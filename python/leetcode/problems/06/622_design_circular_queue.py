class MyCircularQueue:

    def __init__(self, k: int):
        self.Size = 0
        self.MaxSize = k
        self.Data = []
        return

    def enQueue(self, value: int) -> bool:
        # the example does imply enQ is adding to the Rear end ...
        if self.isFull():
            return False
        self.Data.append(value)
        self.Size += 1
        return True

    def deQueue(self) -> bool:
        # ... but the example *DOES NOT* say whether we deQ from Front or Rear.
        # calling it a "queue" *implies* Front, but they did not specify directly.
        if self.isEmpty():
            return False
        del self.Data[0]   # 0 == delete Front; -1 == delete Rear
        self.Size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.Data[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.Data[-1]

    def isEmpty(self) -> bool:
        return self.Size == 0

    def isFull(self) -> bool:
        return self.Size == self.MaxSize        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# NOTE: Runtime 59 ms Beats 55.53%
# NOTE: Memory 17.14 MB Beats 79.57%
