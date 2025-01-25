class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        serverByX = {}
        serverByY = {}

        # count = 0
        for X, row in enumerate(grid):
            for Y, value in enumerate(row):
                if value:
                    cell = (X,Y)
                    serverByX.setdefault(X, set())
                    serverByY.setdefault(Y, set())
                    serverByX[X].add(cell)
                    serverByY[Y].add(cell)
                    # count += 1
        
        print(f'{serverByX=}')
        print(f'{serverByY=}')
        # print(f'{count=}')

        answer = set()
        for X, servers in serverByX.items():
            if len(servers) <= 1:
                continue
            answer |= servers
        for Y, servers in serverByY.items():
            if len(servers) <= 1:
                continue
            answer |= servers

        print(f'{answer=}')
        return len(answer)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 31 ms Beats 27.48%
# NOTE: Memory 19.30 MB Beats 7.74%

# NOTE: re-ran for challenge:
# NOTE: Runtime 27 ms Beats 25.47%
# NOTE: Memory 20.03 MB Beats 11.61%
