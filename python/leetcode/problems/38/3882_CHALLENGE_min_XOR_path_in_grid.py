class Solution:
    def minCost(self, grid: list[list[int]]) -> int:

        @cache
        def DP(x: int, y: int) -> Set[int]:
            me = grid[x][y]
            if (x,y) == (0,0):
                # print(f'DP({x},{y}) {me=}')
                return {me}
            if x < 0 or y < 0:
                return set()
            # print(f'DP({x},{y}) {me=}')
            left = DP(x - 1, y)
            up   = DP(x, y - 1)
            # print(f'DP({x},{y}): {left} {up}')
            answer = {
                X ^ me
                for X in left | up
            }
            # print(f'DP({x},{y}): {answer=}')
            return answer

        m = len(grid)
        n = len(grid[0])
        values = DP(m - 1, n - 1)
        # print(f'{values=}')

        return min(values)

# NOTE: Acceptance Rate 40.0% (medium)

# NOTE: Accepted on second Run (set "or" set, not "plus")
# NOTE: Accepted on fifth Submit (edge case: leak from OOB; Output Exceed *3)
# NOTE: Runtime 1055 ms Beats 84.17%
# NOTE: Memory 292.88 MB Beats 5.00%
