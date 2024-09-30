class Solution:
    @cache
    def cSum4_hashable(self, nums: List[int], target: int) -> int:
        print(f'cS4({target})')
        if target == 0:
            # we've reached the target
            return 1

        if target < 0:
            # we've overshot the target
            return 0
        
        return sum([
            self.combinationSum4(nums, target - N)
            for N in nums
            if N <= target
        ])
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.cSum4_hashable(tuple(nums), target)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 43 ms Beats 39.00%
# NOTE: Memory 16.94 MB Beats 7.51%
