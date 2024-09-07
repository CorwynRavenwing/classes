class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:

        # SHORTCUT 1:
        # we are allowed any number (>=1) of moves.
        # if we move, say, three times, from cell A -> B -> C -> D,
        # our total score will be:
        # B-A + C-B + D-C
        # everything cancels out except for D-A
        # therefore we *do not* have to keep track of multiple possible moves
        # we can merely do one single move, from a cell to any other
        # cell that is *anywhere* below or to its right.
        # This gets rid of the "did I move yet" thing as well
        # as the entire recursion thing.
        # In addition, the cell we want to move to, will always be the
        # cell with the largest score in the allowable portion of the grid.

        # SHORTCUT 2:
        # *do* keep a recursive sum-up of "max number in grid below/right of cell X,Y"
        # ... or possibly of "min number above,left of X,Y inclusive", which is easier
        
        grid_min_by_row = [
            tuple(accumulate(row, min))
            for row in grid
        ]
        # print(f'{grid_min_by_row=}')

        INVERT = lambda x: tuple(zip(*x))

        INV_grid_min_by_row = INVERT(grid_min_by_row)
        # print(f'{INV_grid_min_by_row=}')
        
        INV_grid_min_by_cell = [
            tuple(accumulate(row, min))
            for row in INV_grid_min_by_row
        ]
        # print(f'{INV_grid_min_by_cell=}')

        grid_min_by_cell = INVERT(INV_grid_min_by_cell)
        # print(f'{grid_min_by_cell=}')

        M = len(grid)
        N = len(grid[0])
        print(f'{M=} x {N=} = {M * N}')

        answers = [
            # row -1, same col
            c2 - c1
            for c1row, c2row in zip(grid_min_by_cell, grid[1:])
            for c1, c2 in zip(c1row, c2row)
        ] + [
            # same row, col -1
            c2 - c1
            for c1row, c2row in zip(grid_min_by_cell, grid)
            for c1, c2 in zip(c1row, c2row[1:])
        ]
        # print(f'{answers=}')

        answer = max(answers)
        return answer

# NOTE: A much, much faster run-time than my prior version.
# NOTE: Runtime 1005 ms Beats 95.94%
# NOTE: Memory 34.98 MB Beats 11.81%
