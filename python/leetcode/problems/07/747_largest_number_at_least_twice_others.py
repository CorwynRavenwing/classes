class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        maxVal = max(nums)
        maxIndex = nums.index(maxVal)

        check = list([
            (
                True if N == maxVal
                else True if N * 2 <= maxVal
                else False 
            )
            for N in nums
        ])
        print(f"{check=}")
        if False not in check:
            return maxIndex
        else:
            return -1

