class Solution:
    def maxScore(self, nums: List[int]) -> int:

        nums.sort(reverse=True)
        # I was going to put "all positive numbers, first, in arbitrary order,
        # followed by all negative numbers in order of increasing magnitude"
        # but Hint #1 just gave away the solution :-(
        
        partialSums = tuple(accumulate(nums))
        print(f'{partialSums=}')
        
        positives = len([
            1
            for S in partialSums
            if S > 0
        ])

        return positives
# NOTE: Runtime 585 ms Beats 25.47%
# NOTE: Memory 31.12 MB Beats 46.70%
