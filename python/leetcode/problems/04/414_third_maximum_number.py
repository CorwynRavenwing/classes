class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        def filterAway(nums: List[int], val: int) -> List[int]:
            return list([
                N
                for N in nums
                if N != val
            ])
        
        max_1 = max(nums)
        nums = filterAway(nums, max_1)
        
        if not nums:
            return max_1
        
        max_2 = max(nums)
        nums = filterAway(nums, max_2)
        
        if not nums:
            return max_1

        max_3 = max(nums)
        return max_3

