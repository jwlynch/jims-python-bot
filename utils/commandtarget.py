

class CommandTarget(object):
    def __init__(self):
        super(CommandTarget, self).__init__()
        self._itsNextTarget = None

    def imYourNextTarget(self, aCommandTarget):
        if not isinstance(aCommandTarget, CommandTarget): 
            raise Exception(
                "The object you're trying to send is not the correct type. Did you forget to also inherit from CommandTarget?"
            )

        self._itsNextTarget = aCommandTarget

#
# suggestion for command list for doCommandStr
#
# first, set vars to command strings
#
# cmdFoo = "foo"
# cmdBar = "bar"
#

    def doCommandStr(self, cmdString, *args, **kwargs):
        result = None
        # pass the buck

        if self._itsNextTarget is not None:
            result = self._itsNextTarget.doCommandStr(cmdString, *args, **kwargs)

        return result

#
# doCommandStr suggestion for override
#
# def doCommandStr(self, cmdString, *args, **kwargs)
#     result = None
#
#     (extract from args whatever might be needed for running the command)
#
#     if cmdString = self.cmdFoo:
#         (code for the command gies here, set result to success (0) or raise exception)
#     elif cmdString = self.cmdBar:
#         (code for cmdBar goes here, set result or raise excepton)
#     else:
#         # pass buck to superclass
#         result = super(FooClass, self).doCommandStr(cmdString, *args, **kwargs)
#

