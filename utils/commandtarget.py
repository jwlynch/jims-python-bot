

class CommandTarget(object):
    def __init__(self):
        self._itsNextTarget = None
    
    def imYourNextTarget(self, aCommandTarget):
        if not aComnmandTarget.isinstance(CommandTarget): 
            raise Exception(
                "The object you're trying to send is not the correct type. Did you forget to also inherit from CommandTarget?"
            )
          
        self._itsNextTarget = aCommandTarget

    def doCommand(self, command, args):
        result = None
        # pass the buck

        if self._itsNextTarget is not None:
            result = self._itsNextTarget.doCommand(command, args)

        return result

    def searchCommand(self, cmdString):
        result = None
        if not _itsNextTarget is None:
            result = _itsNextTarget.searchCommand(cmdString)
        
        return result

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
