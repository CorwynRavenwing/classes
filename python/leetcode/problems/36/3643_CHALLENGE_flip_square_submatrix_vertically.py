class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

        x1 = x
        x2 = x + k - 1
        while x1 < x2:
            # print(f'{x1=} {x2=}:')
            for y1 in range(y, y + k):
                # print(f'  swap ({x1},{y1}),({x2},{y1}):')
                A = grid[x1][y1]
                B = grid[x2][y1]

                grid[x1][y1] = B
                grid[x2][y1] = A

                # print(f'  {y1=} {A=} {B=}')

            # move them closer
            x1 += 1
            x2 -= 1

        return grid

# NOTE: Acceptance Rate 79.3% (easy)

# NOTE: Accepted on third Run (fencepost errors)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.56 MB Beats 70.27%
