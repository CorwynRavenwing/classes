class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # per hint #1, two copies of something will XOR themselves away:
        partialXOR = tuple(accumulate(nums, operator.xor))
        return partialXOR[-1]
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 116 ms Beats 30.98%
# NOTE: Memory 19.46 MB Beats 5.91%
