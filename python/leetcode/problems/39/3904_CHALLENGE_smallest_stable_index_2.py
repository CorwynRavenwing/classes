class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        # we borrow some code from #3901:

        MIN = lambda L: tuple(accumulate(L, min))
        MAX = lambda L: tuple(accumulate(L, max))
        REV = lambda L: tuple(reversed(L))

        maxLeft = MAX(nums)
        minRight = REV(MIN(REV(nums)))

        # print(f'{maxLeft =}')
        # print(f'{minRight=}')

        for i, (L, R) in enumerate(zip(maxLeft, minRight)):
            diff = L - R
            stable = (diff <= k)
            # print(f'[{i}]: {L},{R} -> {diff} {stable}')
            if stable:
                return i

        return -1

# NOTE: Acceptance Rate 73.7% (medium)

# NOTE: re-used entirety of prior version
# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output exceeded)
# NOTE: Runtime 199 ms Beats 46.37%
# NOTE: Memory 32.09 MB Beats 68.18%
