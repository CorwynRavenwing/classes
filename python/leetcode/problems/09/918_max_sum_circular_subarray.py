class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        # we borrow some code from #53:

        def max_subarray():
            # Kadane's algorithm

            current_sum = 0
            max_so_far = float('-inf')
            for N in nums:
                current_sum += N
                if max_so_far < current_sum:
                    max_so_far = current_sum
                if current_sum < 0:
                    current_sum = 0
                # print(f'{N=} {current_sum=} {max_so_far=}')
            return max_so_far

        def min_subarray():
            # Kadane's algorithm inverted for Min

            current_sum = 0
            min_so_far = float('+inf')
            for N in nums:
                current_sum += N
                if min_so_far > current_sum:
                    min_so_far = current_sum
                if current_sum > 0:
                    current_sum = 0
                # print(f'{N=} {current_sum=} {min_so_far=}')
            return min_so_far

        MAX_STRAIGHT = max_subarray()
        MAX_WRAPPED = sum(nums) - min_subarray()
        # b/c max + min = total; also, if max is wrapped, min is not
        MAX_ARRAY = max(nums)

        print(f'{MAX_ARRAY=} {MAX_STRAIGHT=} {MAX_WRAPPED=}')
        
        if MAX_ARRAY < 0:
            # all numbers are negative: return the one least-negative number
            return MAX_ARRAY
        else:
            return max(MAX_STRAIGHT, MAX_WRAPPED)

# NOTE: 305 ms; Beats 98.47%

