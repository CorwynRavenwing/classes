class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:

        grid_M = len(grid)
        grid_N = len(grid[0])

        products = [
            [
                []
                for cell in row
            ]
            for row in grid
        ]
        products[0][0] = [grid[0][0]]
        for i in range(1, grid_M):
            products[i][0] = [
                grid[i][0] * P
                for P in set(products[i - 1][0])
            ]
        for j in range(1, grid_N):
            products[0][j] = [
                grid[0][j] * P
                for P in set(products[0][j - 1])
            ]
        for i in range(1, grid_M):
            for j in range(1, grid_N):
                products[i][j] = [
                    grid[i][j] * P
                    for P in set(products[i - 1][j] + products[i][j - 1])
                ]
        print(f'{products=}')
        answers = products[-1][-1]
        print(f'{answers=}')
        A = max(answers)
        if A < 0:
            return -1
        
        mod = 10 ** 9 + 7
        return A % mod

