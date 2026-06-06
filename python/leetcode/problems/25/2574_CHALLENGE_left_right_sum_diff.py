class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        CHOP = lambda L: L[:-1]
        LEFT = lambda L: (0,) + CHOP(tuple(accumulate(L)))
        REV = lambda L: tuple(reversed(L))
        RIGHT = lambda L: REV(LEFT(REV(L)))

        leftsum = LEFT(nums)
        rightsum = RIGHT(nums)
        # print(f'{leftsum =}')
        # print(f'{rightsum=}')

        diffs = [
            abs(A - B)
            for (A, B) in zip(leftsum, rightsum)
        ]
        # print(f'{diffs=}')

        return diffs

# NOTE: Acceptance Rate 88.1% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 74.11%
# NOTE: Memory 19.50 MB Beats 57.43%
