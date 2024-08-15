class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:

        # faster algorithm:
        # start at the end.  If you were to succeed, the last step
        # would be each Nums in its own length-1 subarray,
        # and the step before that would be one of two things:
        # A) one length-2 that adds up to >= m;
        # B) one length-2 that is the entire Nums array.
        # after that point, B) is done, and A) can always be merged
        # with either adjacent number to get larger, since
        # negative numbers are disallowed.

        if len(nums) <= 2:
            return True
        
        priorA = None
        for i, A in enumerate(nums):
            if priorA is not None:
                if A + priorA >= m:
                    return True
            priorA = A
        return False
# NOTE: Runtime 53 ms Beats 48.87%
# NOTE: Memory 16.43 MB Beats 75.94%
