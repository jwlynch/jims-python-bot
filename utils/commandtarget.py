

class CommandTarget(object):
    def __init__(self):
        self._itsNextTarget = None
    
    def imYourNextTarget(self, aCommandTarget):
        if not aComnmandTarget.isinstance(CommandTarget): 
            raise Exception(
                "The object you're trying to send is not the correct type. Did you forget to also inherit from CommandTarget?"
            )
          
        self._itsNextTarget = aCommandTarget
        
    def doCommand(command):
        # pass the buck
        
        if self._itsNextTarget is not None:
            self._itsNextTarget.doCommand(command)