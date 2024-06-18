class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        paths = {}
        # e.g. (0,0): 1
        
        for x in range(m):
            for y in range(n):
                if x == 0 and y == 0:
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

