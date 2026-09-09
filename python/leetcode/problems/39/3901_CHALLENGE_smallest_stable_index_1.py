class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
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
            print(f'[{i}]: {L},{R} -> {diff} {stable}')
            if stable:
                return i

        return -1

# NOTE: Acceptance Rate 68.7% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 6 ms Beats 49.01%
# NOTE: Memory 19.68 MB Beats 9.85%
