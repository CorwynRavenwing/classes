class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        answer = max(nums)  # best of all the 1-element subarrays
        
        accumulator = nums[0]
        for A, B in pairwise(nums):
            if A >= B:
                accumulator = 0
            accumulator += B
            answer = max(answer, accumulator)

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.84 MB Beats 28.05%
