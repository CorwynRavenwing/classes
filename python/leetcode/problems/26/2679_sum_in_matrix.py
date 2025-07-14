class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        
        DESC = lambda L: sorted(L, reverse=True)
        nums_sorted = tuple(map(DESC, nums))
        print(f'{nums_sorted=}')

        nums_groups = tuple(zip(*nums_sorted))
        print(f'{nums_groups}')

        maxes = tuple(map(max, nums_groups))
        print(f'{maxes}')

        return sum(maxes)

# NOTE: Acceptance Rate 59.2% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 103 ms Beats 21.43%
# NOTE: Memory 37.81 MB Beats 12.05%
