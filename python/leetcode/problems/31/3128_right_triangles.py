class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:

        ones_in_rows = tuple(map(sum, grid))
        ones_in_cols = tuple(map(sum, zip(*grid)))
        print(f'{ones_in_rows=}')
        print(f'{ones_in_cols=}')

        answer = [
            (
                ones_in_rows[R] - 1
            ) * (
                ones_in_cols[C] - 1
            )
            for R, row in enumerate(grid)
            for C, val in enumerate(row)
            if val == 1
        ]
        print(f'{answer=}')

        return sum(answer)
# NOTE: Accepted on first Run; Accepted on first Submit
# NOTE: Runtime 2286 ms Beats 78.17%
# NOTE: Memory 97.68 MB Beats 5.68%
