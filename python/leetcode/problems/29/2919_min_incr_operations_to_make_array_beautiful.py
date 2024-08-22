class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        
        # [43,31,14,4], 45
        
        # if every subarray with size *exactly* 3 has its maximum
        # element >= K, then any subarray with size *GT* 3 will
        # have this hold as well.  So we will Without Loss of Generality
        # only check for the simpler condition.

        minIncrementEndingAt = [None] * len(nums)
        for i in range(3):
            minIncrementEndingAt[i] = max(0, k - nums[i])
        # print(f'{minIncrementEndingAt=}')

        for i in range(3, len(nums)):
            # print(f'{i=}')
            scores = [
                minIncrementEndingAt[j]
                for j in range(i-3, i)
            ]
            # print(f'  {scores=}')
            minIncrementEndingAt[i] = min(scores) + max(0, k - nums[i])
        # print(f'{minIncrementEndingAt=}')

        scores = [
            minIncrementEndingAt[j]
            for j in range(len(nums) - 3, len(nums))
        ]
        print(f'End: {scores=}')

        return min(scores)

# NOTE: Runtime 774 ms Beats 41.13%
# NOTE: Memory 31.75 MB Beats 72.58%
