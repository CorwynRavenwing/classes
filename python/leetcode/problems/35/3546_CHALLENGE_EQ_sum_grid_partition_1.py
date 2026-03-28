class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        # NOTE 1: since we are summing an entire section,
        # either horizontally or vertically, we may therefore,
        # without loss of generality, first sum the rows or columns
        # in the opposite direction from the dividing line,
        # then dividing the resultant 1-dimentional array.

        # NOTE 2: after summing the rows and dividing the
        # remainder, to sum the columns we can merely invert
        # the grid and run the same row-based code again.

        # NOTE 3: to split a single array into two equal parts,
        # perform partial sums; partial[-1] is the grand total;
        # look for total//2 existing in the array.

        INV = lambda G: tuple(map(tuple, zip(*G)))

        SUM = lambda G: tuple(map(sum, G))

        ACC = lambda L: tuple(accumulate(L))

        def check_grid(G: List[List[int]]) -> bool:
            print(f'--------------------')
            sum_grid = SUM(G)
            print(f'{sum_grid=}')

            partialSum = ACC(sum_grid)
            print(f'{partialSum=}')

            total = partialSum[-1]
            half = total // 2
            print(f'{total=} {half=}')

            if (half * 2) != total:
                return False

            return half in partialSum

        return check_grid(grid) or check_grid(INV(grid))

# NOTE: Acceptance Rate 42.3% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case w/odd total)
# NOTE: Runtime 118 ms Beats 78.77%
# NOTE: Memory 49.50 MB Beats 15.07%
