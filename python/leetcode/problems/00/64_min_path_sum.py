class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        minGrid = [
            [None] * n
            for row in grid
        ]
        minGrid[0][0] = grid[0][0]
        print(f'start: {minGrid=}')
        for i in range(1, m):
            minGrid[i][0] = grid[i][0] + minGrid[i - 1][0]
        print(f'i when j=0: {minGrid=}')
        for j in range(1, n):
            minGrid[0][j] = grid[0][j] + minGrid[0][j - 1]
        print(f'j when i=0: {minGrid=}')
        for i in range(1, m):
            for j in range(1, n):
                minGrid[i][j] = grid[i][j] + min([
                    minGrid[i - 1][j],
                    minGrid[i][j - 1],
                ])
        print(f'all i and j: {minGrid=}')
        
        return minGrid[-1][-1]

# NOTE: Runtime 134 ms Beats 12.18%
# NOTE: Memory 19.10 MB Beats 14.99%
