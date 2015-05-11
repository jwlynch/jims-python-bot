

class CommandTarget(object):
    def __init__(self):
        super(CommandTarget, self).__init__()
        self._itsNextTarget = None
    
    def imYourNextTarget(self, aCommandTarget):
        if not aComnmandTarget.isinstance(CommandTarget): 
            raise Exception(
                "The object you're trying to send is not the correct type. Did you forget to also inherit from CommandTarget?"
            )
          
        self._itsNextTarget = aCommandTarget

#
# suggestion for command list for searchCommand
#
# first, set vars to command numbers
#
# cmdFoo = 1
# cmdBar = 3
#
# then, make a dict where the keys are the command strings that come from the bot
#
# commands = {"foo": cmdFoo, "bar": cmdBar}
#
# then, the suggested code for searchCommand will pick them up. use the symbolic names in doCommsnd().
#

    def doCommand(self, command, args):
        result = None
        # pass the buck

        if self._itsNextTarget is not None:
            result = self._itsNextTarget.doCommand(command, args)

        return result

#
# doCommand suggestion for override
#
# def doCommand(self, command, args)
#     result = None
#
#     (extract from args whatever might be needed for running the command)
#
#     if command = self.cmdFoo:
#         (run the command, set result to success (0) or raise exception)
#     elif command = self.cmdBar:
#         (run cmdBar, set result or raise excepton)
#     else:
#         # pass buck to superclass
#         result = super(FooClass, self).doCommand(command, args)
#

    def searchCommand(self, cmdString):
        result = None
        if not self._itsNextTarget is None:
            result = self._itsNextTarget.searchCommand(cmdString)
        
        return result

#
# searchCommand suggestion for override
#
# def searchCommand(self, cmdString)
#     result = None
#     for key in self.commands:
#         if key == cmdString:
#             result = self.commands[cmdString]
#
#     if result == None:
#         result = super(FooClass, self).searchCommand(cmdString)
#
#     return result
#

    def doCommandStr(self, cmdString, args):
        result = None
        cmd = self.searchCommand(cmdString)
        
        if cmd is not None:
            result = self.doCommand(cmd, args)

        return result

# one way:
#
# define a hash with string command-name keys that go to command numbers,
# and have searchCommand use that, then define doCommand as an if...elif
# structure where each command number is tested. doCommand should return
# None if it doesn't result in a command being executed
