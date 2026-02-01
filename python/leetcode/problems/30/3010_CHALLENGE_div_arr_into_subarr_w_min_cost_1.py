class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        # NOTE: the first subarray must start with the first element
        # of the array.  the other two subarrays in optimal answers
        # will start with the two lowest numbers that are *not*
        # the first element.

        costs = 0
        costs += nums.pop(0)
        nums.sort()
        costs += nums.pop(0)
        costs += nums.pop(0)

        return costs

# NOTE: Acceptance Rate 67.0% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.45 MB Beats 15.15%
