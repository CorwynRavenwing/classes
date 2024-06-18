class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:

        M = len(grid)
        N = len(grid[0])
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                print(f'({i},{j})={val}')
                if i+1 < M and val != grid[i + 1][j]:
                    print(f'  {val} != {grid[i + 1][j]=}')
                    return False
                if j+1 < N and val == grid[i][j + 1]:
                    print(f'  {val} == {grid[i][j + 1]=}')
                    return False
        return True

