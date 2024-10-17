class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        # there is no relevant difference between the North and South skylines,
        # nor between the East and West skylines.  We will deal with only one.

        X_skyline = tuple(map(max, grid))
        Y_skyline = tuple(map(max, zip(*grid)))
        print(f'{X_skyline=}')
        print(f'{Y_skyline=}')

        allowed = [
            [
                min(X_height, Y_height)
                for Y, Y_height in enumerate(Y_skyline)
            ]
            for X, X_height in enumerate(X_skyline)
        ]
        print(f'{allowed=}')

        print(f'{grid   =}')

        changes = [
            [
                allow_value - value
                for value, allow_value in zip(row, allow_row)
            ]
            for row, allow_row in zip(grid, allowed)
        ]
        print(f'{changes=}')

        return sum(map(sum, changes))

# NOTE: Accepted on first Submit
# NOTE: Runtime 67 ms Beats 51.96%
# NOTE: Memory 16.88 MB Beats 11.48%
