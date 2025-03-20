class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        flips = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                try:
                    nums[i + 0] ^= 1
                    nums[i + 1] ^= 1
                    nums[i + 2] ^= 1
                    flips += 1
                except IndexError:
                    return -1
        return flips

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 100 ms Beats 68.38%
# NOTE: Memory 21.79 MB Beats 20.05%
