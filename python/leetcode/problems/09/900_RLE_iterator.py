class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.Data = encoding
        return

    def next(self, n: int) -> int:
        print(f'next({n}):')
        print(f'  A: {self.Data}')
        try:
            while n > self.Data[0]:
                n -= self.Data[0]
                del self.Data[:2]
                print(f'  B: {self.Data}')
        except IndexError:
            return -1
        
        while not self.Data[0]:
            del self.Data[:2]
            print(f'  C: {self.Data}')
        
        self.Data[0] -= n
        print(f'  D: {self.Data}')
        return self.Data[1]

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)

# NOTE: Accepted on first Submit
# NOTE: Runtime 43 ms Beats 37.92%
# NOTE: Memory 17.77 MB Beats 6.43%
