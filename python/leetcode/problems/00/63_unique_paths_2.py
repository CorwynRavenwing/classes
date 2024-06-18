class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # we reuse much of the code from #62:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        paths = {}
        # e.g. (0,0): 1
        
        for x in range(m):
            for y in range(n):
                if obstacleGrid[x][y] == 1:
                    paths[(x, y)] = 0
                elif x == 0 and y == 0:
                    paths[(x, y)] = 1
                elif x == 0:
                    paths[(x, y)] = paths[(x, y - 1)]
                elif y == 0:
                    paths[(x, y)] = paths[(x - 1, y)]
                else:
                    paths[(x, y)] = (
                        paths[(x, y - 1)] + paths[(x - 1, y)]
                    )
        return paths[m - 1, n - 1]

