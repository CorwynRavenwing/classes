class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        ACC = lambda L: tuple(accumulate(L))
        INV = lambda G: tuple(map(tuple, zip(*G)))
        # print(f'{INV(grid)=}')

        Ysums = tuple(map(ACC, grid))
        # print(f'{Ysums=}')

        invYsums = INV(Ysums)
        # print(f'{invYsums=}')

        Xsums = tuple(map(ACC, invYsums))
        # print(f'{Xsums=}')

        sums = [
            N
            for row in Xsums
            for N in row
            if N <= k
        ]
        # print(f'{sums=}')

        return len(sums)

# NOTE: Acceptance Rate 58.8% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (title/requirements conflict; Output Exceeded)
# NOTE: Runtime 214 ms Beats 90.34%
# NOTE: Memory 121.70 MB Beats 15.17%
