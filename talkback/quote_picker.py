from random import choice

from utils import commandtarget

class QuotePicker(commandtarget.CommandTarget):

    # overrides from CommandTarget

    cmdQuote = 1
    commands = {"quote": cmdQuote}

    # return 0 on success
    def doCommand(self, command, args):
        result = None
        sendTo = None
        protocol = None

        if command == self.cmdQuote:
            if "sendTo" in args:
                sendTo = args["sendTo"]

                if "protocol" in args:
                    protocol = args["protocol"]
                    protocol.msg(sendTo, "command quote")
                    result = 0 # success
                else:
                    pass # didn't get protocol from args
            else:
                pass # didn't get sendTo from args
        # elif test for other commands this class instance responds to
        else:
            result = super(TalkBackBot, self).doCommand(command, args)

        return result

    def __init__(self, quotes_filename):
        """Initialize our QuotePicker class"""
        with open(quotes_filename) as quotes_file:
            self.quotes = quotes_file.readlines()

    def pick(self):
        """Return a random quote."""
        return choice(self.quotes).strip()
