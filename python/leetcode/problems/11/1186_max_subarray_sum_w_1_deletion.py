class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        
        # we borrow some code from #918:

        def max_subarray(nums: List[int]):
            if max(nums) < 0:
                # can't have empty subarray:
                # return least-bad single element
                return max(nums)
            
            # Kadane's algorithm

            current_sum_nodeletes = 0
            current_sum_1_del = 0
            max_so_far = float('-inf')
            for N in nums:
                current_sum_1_del = max(
                    current_sum_nodeletes,      # skip this one
                    current_sum_1_del + N,   # cant skip any more
                )
                current_sum_nodeletes = max(
                    current_sum_nodeletes + N,
                    N
                )
                max_so_far = max(
                    max_so_far,
                    current_sum_nodeletes,
                    current_sum_1_del,
                )
                print(f'{N=} {current_sum_nodeletes=} {current_sum_1_del=} {max_so_far=}')
            return max_so_far

        return max_subarray(arr)   # no deletions

