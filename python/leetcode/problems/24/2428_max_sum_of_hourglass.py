class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        M = len(grid)
        N = len(grid[0])

        answer = []
        for X in range(1, M - 1):
            for Y in range(1, N - 1):
                print(f'[{X},{Y}]:')
                prev = grid[X - 1][Y - 1:Y + 2]
                this = grid[X][Y]
                next = grid[X + 1][Y - 1:Y + 2]
                print(f'  {prev}')
                print(f'  {(0, this, 0,)}')
                print(f'  {next}')
                answer.append(
                    sum(prev + [this] + next)
                )
        print(f'\n{answer=}')
        return max(answer)

# NOTE: Accepted on second Run (typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 341 ms Beats 5.22%
# NOTE: Memory 20.80 MB Beats 6.79%
