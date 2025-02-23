class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        # we borrow some code from #2149:

        group_LT = [N for N in nums if N < pivot]
        group_EQ = [N for N in nums if N == pivot]
        group_GT = [N for N in nums if N > pivot]
        print(f'{group_LT=}')
        print(f'{group_EQ=}')
        print(f'{group_GT=}')

        return group_LT + group_EQ + group_GT

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 67 ms Beats 14.06%
# NOTE: Memory 34.58 MB Beats 57.95%
