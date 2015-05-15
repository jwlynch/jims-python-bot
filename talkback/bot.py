import collections

from twisted.internet import protocol
from twisted.python import log
from twisted.words.protocols import irc

from utils import commandtarget
from quote_picker import QuotePicker

class TalkBackBot(irc.IRCClient, commandtarget.CommandTarget):
    # overrides from IRCClient

    commands = {}

    def __init__(self):
        super(TalkBackBot, self).__init__()

        self.quotepicker = QuotePicker("quotes.txt")
        self.imYourNextTarget(self.quotepicker)

    def connectionMade(self):
        """Called when a connection is made."""
        self.nickname = self.factory.nickname
        self.realname = self.factory.realname
        self.prefixCmdTriggerChar = self.factory.prefixCmdTriggerChar
        irc.IRCClient.connectionMade(self)
        log.msg("connectionMade")

    def connectionLost(self, reason):
        """Called when a connection is lost."""
        irc.IRCClient.connectionLost(self, reason)
        log.msg("connectionLost {!r}".format(reason))

    # callbacks for events

    def signedOn(self):
        """Called when bot has successfully signed on to server."""
        log.msg("Signed on")

        self.channelUsers = collections.defaultdict(set)
        self.nickPrefixes = ''.join(prefix for prefix, _ in self.supported.getFeature('PREFIX').itervalues())

        if self.nickname != self.factory.nickname:
            log.msg('Your nickname was already occupied, actual nickname is '
                    '"{}".'.format(self.nickname))

        self.join(self.factory.channel)


    def joined(self, channel):
        """Called when the bot joins the channel."""
        log.msg("[{nick} has joined {channel}]"
                .format(nick=self.nickname, channel=self.factory.channel,))

    def privmsg(self, user, channel, msg):
        """Called when the bot receives a message."""

        log.msg("privmsg ( {user}, {channel}, {msg} )"
                .format(user=user, channel=channel, msg=msg,))

        sendTo = None
        prefix = ''
        senderNick = user.split('!', 1)[0]
        msg = msg.strip()
        if channel == self.nickname:
            log.msg("privmsg: channel == self.nickname")
            # /MSG back
            sendTo = senderNick
        elif msg.startswith(self.nickname):
            log.msg("privmsg: msg.startswith*self.nickname)")
            # Reply back on the channel
            sendTo = channel
            prefix = senderNick + ': '
        else:
            log.msg("privmsg: else")
            msg = msg.lower()
            sendTo = channel

        if sendTo:
            if msg.startswith(self.prefixCmdTriggerChar):
                cmd = msg[1:]
                cmdList = cmd.split()
                args = []

                if len(cmdList) > 1:
                    args = cmdList[1:]

                cmdNum = self.searchCommand(cmdList[0])

                if cmdNum is not None:
                    result = self.doCommand(cmdNum, *args, sendTo=sendTo, protocol=self, prefix=prefix)
                else:
                    self.msg(sendTo, "command " + cmdList[0] + " not found")

    def irc_RPL_NAMREPLY(self, prefix, params):
        channel = params[2].lower()
        self.channelUsers[channel].update(nick.lstrip(self.nickPrefixes) for nick in params[3].split(' '))

    def userJoined(self, user, channel):
        nick, _, host = user.partition('!')
        self.channelUsers[channel.lower()].add(nick)

    def userLeft(self, user, channel):
        nick, _, host = user.partition('!')
        self.channelUsers[channel.lower()].discard(nick)

    def userQuit(self, user, quitMessage):
        nick, _, host = user.partition('!')
        
        for users in self.channelUsers.itervalues():
            users.discard(nick)

    def userKicked(self, kickee, channel, kicker, message):
        nick, _, host = kickee.partition('!')
        self.channelUsers[channel.lower()].discard(nick)

    def userRenamed(self, oldname, newname):
        for users in self.channelUsers.itervalues():
            if oldname in users:
                users.discard(oldname)
                users.add(newname)

class TalkBackBotFactory(protocol.ClientFactory):
    protocol = TalkBackBot

    # instantiate the TalkBackBot IRC protocol

    def __init__(self, channel, nickname, realname, quotes, triggers, prefixCmdTriggerChar):
        """Initialize the bot factory with our settings."""
        self.channel = channel
        self.nickname = nickname
        self.realname = realname
        self.quotes = quotes
        self.triggers = triggers
        self.prefixCmdTriggerChar = prefixCmdTriggerChar
