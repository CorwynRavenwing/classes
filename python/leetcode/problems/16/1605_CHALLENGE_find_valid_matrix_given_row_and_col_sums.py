class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        grid = [
            [
                0
                for j in range(len(colSum))
            ]
            for i in range(len(rowSum))
        ]

        while max(rowSum + colSum) > 0:
            i = rowSum.index(max(rowSum))
            j = colSum.index(max(colSum))
            R = rowSum[i]
            C = colSum[j]
            change = min(R, C)
            print(f'[{i},{j}] ({R},{C})')
            grid[i][j] += change
            rowSum[i] -= change
            colSum[j] -= change

        return grid
# NOTE: Runtime 530 ms; Beats 70.04%
# NOTE: Memory 22.07 MB; Beats 14.08%
