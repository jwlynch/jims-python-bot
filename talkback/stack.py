

class Stack(object):
    def __init__(self):
        self.stack = []
        self.dex = 0

    def push(self, obj):
        self.stack.append(obj)
        self.dex += 1

    def pop(self):
        result = self.stack.pop()
        self.dex -= 1
        return result

    def pick(self, dex):
        pass
