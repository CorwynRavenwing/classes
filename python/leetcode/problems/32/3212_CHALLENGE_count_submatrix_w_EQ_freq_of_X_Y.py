class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
        grid = [
            [
                (
                    1 if N == 'X'
                    else 0 if N == '.'
                    else -1 if N == 'Y'
                    else '?'
                )
                for N in row
            ]
            for row in grid
        ]
        # print(f'{grid=}')

        POS = lambda L: [max(X, 0) for X in L]
        Xs = tuple(map(POS, grid))
        # print(f'{Xs=}')

        # NOTE: we borrow some code from #3070:
        ACC = lambda L: tuple(accumulate(L))
        INV = lambda G: tuple(map(tuple, zip(*G)))

        def matrixSums(G: List[List[int]]) -> List[List[int]]:
            Ysums = tuple(map(ACC, G))
            invYsums = INV(Ysums)
            invXsums = tuple(map(ACC, invYsums))
            Xsums = INV(invXsums)
            return Xsums
        
        sums = matrixSums(grid)
        Xsums = matrixSums(Xs)
        # print(f'{sums=}')
        # print(f'{Xsums=}')

        crosses = [
            (N, Xn)
            for (row, Xrow) in zip(sums, Xsums)
            for (N, Xn) in zip(row, Xrow)
        ]
        # print(f'{crosses=}')

        crossSums = [
            (N, Xn)
            for (N, Xn) in crosses
            if N == 0 and Xn > 0
        ]
        # print(f'{crossSums=}')

        return len(crossSums)


# NOTE: Acceptance Rate 51.9% (medium)

# NOTE: Accepted on second Run (polarity issue)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 877 ms Beats 65.59%
# NOTE: Memory 249.16 MB Beats 5.38%
