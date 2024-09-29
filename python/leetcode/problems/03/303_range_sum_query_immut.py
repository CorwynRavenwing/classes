class NumArray:

    def __init__(self, nums: List[int]):
        self.partialSums = (0,) + tuple(accumulate(nums))
        # throw away Nums itself

    def sumRange(self, left: int, right: int) -> int:
        return self.partialSums[right + 1] - self.partialSums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# NOTE: Accepted on first Submit
# NOTE: Runtime 72 ms Beats 53.66%
# NOTE: Memory 20.17 MB Beats 52.59%
