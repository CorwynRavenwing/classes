class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        self.nums = self.nums[-self.k:]
        # print(f'{k=} {len(self.nums)=}')

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        # print(f'{self.k=} {len(self.nums)=}')
        # print(f'{self.nums[-self.k]=}')
        if self.k < len(self.nums):
            ignore = self.nums.pop(0)
        #     print(f'{ignore=}')
        # else:
        #     print(f'not enough values yet')
        return self.nums[-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# NOTE: Runtime 104 ms Beats 12.74%
# NOTE: Memory 20.54 MB Beats 53.25%
