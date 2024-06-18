class Solution:

    data = []

    def __init__(self, w: List[int]):
        print(f'DEBUG: {self.data=}')
        self.data = [None] * len(w)
        print(f'DEBUG: {w=} {len(self.data)=}')
        print(f'DEBUG: {self.data=}')
        for index, val in enumerate(w):
            new_val = val + (
                self.data[index - 1]
                if index
                else 0
            )
            self.data[index] = new_val
            print(f'DEBUG: {index=} {val=} {new_val=}')
        print(f'DEBUG: {self.data=}')
        return

    def pickIndex(self) -> int:
        max_val = self.data[-1]
        print(f'DEBUG: search [1..{max_val}]')
        # RN = random.randrange(max_val)
        RN = random.randint(1, max_val)
        # RN = random.random() * max_val
        index = bisect.bisect_left(self.data, RN)
        print(f'  {RN=} {index=}')
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

