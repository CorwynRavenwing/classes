class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        M = len(grid)
        N = len(grid[0])

        INV = lambda G: tuple(map(tuple, zip(*G)))

        used_Y = [
            [
                grid[X][Y:Y + k]
                for Y in range(N - k + 1)
            ]
            for X in range(M)
        ]
        print(f'{used_Y=}')
        inv_used_Y = INV(used_Y)
        print(f'{inv_used_Y=}')

        inv_used_X = [
            [
                [
                    Num
                    # yes, X/Y are backwards because of INV
                    for Group in inv_used_Y[Y][X:X + k]
                    for Num in Group
                ]
                for X in range(M - k + 1)
            ]
            for Y in range(N - k + 1)
        ]
        print(f'{inv_used_X=}')
        used_X = INV(inv_used_X)
        print(f'{used_X=}')

        TSS = [
            [
                tuple(sorted(set(values)))
                for values in row
            ]
            for row in used_X
        ]
        print(f'{TSS=}')

        DIFF = lambda P: P[1] - P[0]

        diffs = [
            [
                tuple(map(DIFF, pairwise(values)))
                for values in row
            ]
            for row in TSS
        ]
        print(f'{diffs=}')

        answer = [
            [
                min(values, default=0)
                for values in row
            ]
            for row in diffs
        ]
        print(f'{answer=}')

        return answer

# NOTE: Acceptance Rate 78.9% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 94 ms Beats 8.31%
# NOTE: Memory 22.81 MB Beats 15.95%
