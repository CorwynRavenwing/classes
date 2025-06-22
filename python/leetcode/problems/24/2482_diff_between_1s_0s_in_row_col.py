class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        # NOTE: diff[i][j] = onesRow[0] + onesCol[0] - zerosRow[0] - zerosCol[0]
        # if we define deltaRow[i] === onesRow[i] - zerosRow[i]
        # and define deltaCol[j] === onesCol[j] - zerosCol[j], then:
        # diff[i][j] === deltaRow[i] + deltaCol[j]

        # NOTE: ones_X === sum(X)
        # NOTE: zeros_X === len(X) - ones_X

        # NOTE: therefore delta_X === ones_X - zeros_X
        # === ones_X - (len_X - ones_X)
        # === ones_X + ones_X - len_X
        # === (2 * ones_X) - len_X
        # therefore zeros_X need not be calculated

        M = len(grid)       # i range, ZRow
        N = len(grid[0])    # j range, ZCol

        ONES = lambda G: tuple(map(sum, G))
        INV = lambda G: tuple(zip(*G))
        # print(f'DEBUG: {INV(grid)=}')

        onesRow = ONES(grid)
        print(f'{onesRow=}')
        onesCol = ONES(INV(grid))
        print(f'{onesCol=}')

        deltaRow = [(ones + ones - M) for ones in onesRow]
        deltaCol = [(ones + ones - N) for ones in onesCol]

        diff = [
            [
                rowDiff + colDiff
                for colDiff in deltaCol
            ]
            for rowDiff in deltaRow
        ]
        return diff

# NOTE: Accepted on second Run (variable name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 155 ms Beats 75.00%
# NOTE: Memory 55.44 MB Beats 13.33%
