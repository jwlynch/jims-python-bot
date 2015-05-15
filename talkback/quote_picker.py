from random import choice

from utils import commandtarget

class QuotePicker(commandtarget.CommandTarget):

    # overrides from CommandTarget

    cmdQuote = 1
    commands = {"quote": cmdQuote}

    # return 0 on success
    def doCommand(self, command, *args, **kwargs):
        result = None
        sendTo = None
        protocol = None

        if command == self.cmdQuote:
            if "sendTo" in kwargs:
                sendTo = kwargs["sendTo"]

                if "protocol" in kwargs:
                    protocol = kwargs["protocol"]
                    prefix = kwargs["prefix"]
                    protocol.msg(sendTo, prefix + self.pick())
                    result = 0 # success
                else:
                    pass # didn't get protocol from args
            else:
                pass # didn't get sendTo from args
        # elif test for other commands this class instance responds to
        else:
            result = super(TalkBackBot, self).doCommand(command, *args, **kwargs)

        return result

    # methods for this class (QuotePicker)

    def __init__(self, quotes_filename):
        super(QuotePicker, self).__init__()

        """Initialize our QuotePicker class"""
        with open(quotes_filename) as quotes_file:
            self.quotes = quotes_file.readlines()

    def pick(self):
        """Return a random quote."""
        return choice(self.quotes).strip()
