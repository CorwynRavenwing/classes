class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        # start with most negative number
        for n in nums:
            if n > 0:
                # no other negative numbers exist
                break
            if -n in nums:
                # return its positive
                return -n
        return -1
        
