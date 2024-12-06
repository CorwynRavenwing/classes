class Solution:

    # we borrow some code from #53:

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

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        negativeNums = [-N for N in nums]
        return max([
            self.maxSubArray(nums),
            self.maxSubArray(negativeNums),
        ])

# NOTE: re-used entire previous version, adding only clue code
# NOTE: Accepted on second Run (function-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 23 ms Beats 89.85%
# NOTE: Memory 28.53 MB Beats 38.93%
