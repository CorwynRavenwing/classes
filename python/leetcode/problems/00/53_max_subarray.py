class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

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

# NOTE: 484 ms; Beats 93.27%

