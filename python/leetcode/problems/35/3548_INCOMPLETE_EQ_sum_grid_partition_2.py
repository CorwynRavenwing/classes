class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        # we borrow some code from #3546:

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
            lefthalf = total // 2
            righthalf = total - lefthalf
            print(f'{total=} {lefthalf=} {righthalf=}')

            if (half * 2) != total:
                return False

            return half in partialSum

        return check_grid(grid) or check_grid(INV(grid))


# NOTE: Acceptance Rate 23.9% (HARD)

# NOTE: need to add the delete-one-number idea.
# NOTE: can delete *any* value in a 2x2 or larger section;
# NOTE: can delete only *end* values in a 1xN or Nx1 section.
# NOTE: wrong answer until that is written
