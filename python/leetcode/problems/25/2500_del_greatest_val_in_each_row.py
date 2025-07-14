class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        # we borrow some code from #2679
        # (... which, oddly, is a Medium)
        
        DESC = lambda L: sorted(L, reverse=True)
        grid_sorted = tuple(map(DESC, grid))
        print(f'{grid_sorted=}')

        grid_groups = tuple(zip(*grid_sorted))
        print(f'{grid_groups}')

        maxes = tuple(map(max, grid_groups))
        print(f'{maxes}')

        return sum(maxes)

# NOTE: Acceptance Rate 79.1% (easy)

# NOTE: used exact same code as prior version, with variable renames
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 9 ms Beats 41.35%
# NOTE: Memory 18.23 MB Beats 14.63%
