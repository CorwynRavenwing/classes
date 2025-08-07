class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        
        # Hint 1 is an inescapable fact of the rule requiring
        # exactly n-1 moves
        
        # Hint 2 follows from these facts:
        # A) the first child's path is the absolute maximum
        # extent of each of the other children.  Then *can*
        # intersect the path, but they cannot *cross* it.
        # B) any path that does intersect the first child's path,
        # will necessarily be worse than any path that does *not*
        # so intersect, because the first child will have
        # collected all the points before she gets there.
        # Therefore an *optimal* path will not intersect the
        # first child's path except for the lower-right target corner.

        N = len(fruits)
        M = len(fruits[0])
        assert N == M

        child_1 = 0
        for i in range(N):
            child_1 += fruits[i][i]
            fruits[i][i] = 0
        print(f'Child 1: {child_1}')

        def legalPos(i: int, j: int) -> bool:
            return (0 <= i < N) and (0 <= j < N)

        @cache
        def DP(flag: int, i: int, j: int) -> int:
            if not legalPos(i, j):
                # print(f'DP({flag},{i},{j}): OOB')
                return 0
            if i == j:
                # print(f'DP({flag},{i},{j}): diag')
                return 0
            if i > j:
                # print(f'DP({flag},{i},{j}): cross')
                return 0
            # print(f'DP({flag},{i},{j}):')
            answers = [
                DP(flag, i + 1, j - 1),
                DP(flag, i + 1, j),
                DP(flag, i + 1, j + 1),
            ]
            # print(f'DP({flag},{i},{j}): {fruits[i][j]} + {answers}')
            recurse = max(answers)
            return fruits[i][j] + recurse
        
        child_2 = DP(2, 0, N - 1)
        print(f'Child 2: {child_2}')

        # transpose fruits array
        fruits = tuple(map(tuple, zip(*fruits)))
        # print(f'DEBUG: transposed {fruits=}')

        child_3 = DP(3, 0, N - 1)
        print(f'Child 3: {child_3}')

        return child_1 + child_2 + child_3

# NOTE: Acceptance Rate 40.7% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (edge case, Output Exceeded)
# NOTE: Runtime 1479 ms Beats 28.07%
# NOTE: Memory 304.32 MB Beats 12.28%
