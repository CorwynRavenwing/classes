class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:

        maxFromLeft = [None] * len(nums)
        for i, N in enumerate(nums):
            if i == 0:
                maxFromLeft[i] = nums[i]
            else:
                maxFromLeft[i] = max(nums[i], maxFromLeft[i - 1])
        print(f'{maxFromLeft=}')
        assert None not in maxFromLeft

        minFromRight = [None] * len(nums)
        for i, N in reversed(list(enumerate(nums))):
            if i == len(nums) - 1:
                minFromRight[i] = nums[i]
            else:
                minFromRight[i] = min(nums[i], minFromRight[i + 1])
        print(f'{minFromRight=}')
        assert None not in minFromRight

        for i in range(1, len(nums)):
            L = maxFromLeft[i - 1]
            R = minFromRight[i]
            if L <= R:
                left = nums[:i]
                right = nums[i:]
                print(f'{i=} {left=} {right=}')
                return i

        return -1

