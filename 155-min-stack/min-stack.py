class MinStack:

    def __init__(self):
        self.normalStack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.normalStack.append(value)
        if not self.minStack or self.minStack[-1] >= value:
            self.minStack.append(value)

    def pop(self) -> None:
        a = self.normalStack.pop()
        if a == self.minStack[-1]:
            self.minStack.pop() 

    def top(self) -> int:
        return self.normalStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()