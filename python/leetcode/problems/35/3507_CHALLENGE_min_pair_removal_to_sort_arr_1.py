class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        IS_SORTED = lambda L: (tuple(L) == tuple(sorted(L)))

        PAIRS = lambda L: tuple(pairwise(L))
        SUMS = lambda L: tuple(map(sum, PAIRS(L)))

        def min_sum_idx(L: List[int]) -> int:
            Sums = SUMS(L)
            minSum = min(Sums)
            return Sums.index(minSum)

        steps = 0
        print(f'{steps}: {nums}')
        while not IS_SORTED(nums):
            idx = min_sum_idx(nums)
            left = nums[:idx]
            (A, B) = nums[idx:idx+2]
            right = nums[idx+2:]
            Sum = A + B
            print(f'  @{idx} ({A}+{B}) -> {Sum}')
            nums = left + [Sum] + right
            steps += 1
            print(f'{steps}: {nums}')

        return steps

# NOTE: Acceptance Rate 56.4% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case: 1 value)
# NOTE: Runtime 43 ms Beats 5.08%
# NOTE: Memory 19.42 MB Beats 8.08%
