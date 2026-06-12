class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        
        # NOTE: since all numbers are >0, the value
        # ( === max(subarr) - min(subarr) ) of any subarray
        # cannot possibly be greater than the vaue
        # of the entire array.
        # Therefore always choose the entire array

        return k * (max(nums) - min(nums))
        # NOTE: yes, one-linter with 5 lines of explanation

# NOTE: Acceptance Rate 71.8% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 5 ms Beats 92.13%
# NOTE: Memory 26.65 MB Beats 14.96%
