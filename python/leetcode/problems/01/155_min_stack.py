class MinStack:

    def __init__(self):
        self.minStack = []
        self.numStack = []
        return

    def push(self, val: int) -> None:
        if not self.minStack:
            Min = val
        else:
            Min = self.minStack[-1]
            Min = min(Min, val)
        self.minStack.append(Min)
        self.numStack.append(val)
        return

    def pop(self) -> None:
        ignore = self.minStack.pop()
        Num = self.numStack.pop()
        return Num

    def top(self) -> int:
        Num = self.numStack[-1]
        return Num

    def getMin(self) -> int:
        Min = self.minStack[-1]
        return Min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# NOTE: Accepted on first Submit
# NOTE: Runtime 53 ms Beats 66.92%
# NOTE: Memory 20.62 MB Beats 25.89%
