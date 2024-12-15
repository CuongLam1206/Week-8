class Allstack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.size = 0

    def initial(self, capacity):
        self.__capacity = capacity

    def Empty(self):
        return self.size == 0

    def Fulls(self):
        return self.size == self.capacity

    def pushes(self, value):
        if self.Fulls():
            return
        self.stack.append(value)
        self.size += 1

    def pops(self):
        if self.Empty():
            return
        self.size -= 1
        return self.stack.pop()

    def tops(self):
        if self.Empty():
            return
        return self.stack[-1]



stack1 = Allstack(capacity=5)
stack1.pushes(1)
stack1.pushes(2)
print(stack1.Fulls())
print(stack1.tops())
print(stack1.pops())
print(stack1.tops())
print(stack1.pops())
print(stack1.Empty())