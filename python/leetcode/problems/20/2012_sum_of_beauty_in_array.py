class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:

        maxLeft = [None] * len(nums)
        maxLeft[0] = nums[0]
        minRight = [None] * len(nums)
        minRight[-1] = nums[-1]
        for i in range(1, len(nums)):
            maxLeft[i] = max(nums[i], maxLeft[i - 1])
        print(f'{maxLeft=}')
        for j in reversed(range(0, len(nums) - 1)):
            minRight[j] = min(nums[j], minRight[j + 1])
        print(f'{minRight=}')

        beauty = 0
        for k in range(1, len(nums) - 1):
            if maxLeft[k - 1] < nums[k] < minRight[k + 1]:
                print(f'{k}: 2')
                beauty += 2
            elif nums[k - 1] < nums[k] < nums[k + 1]:
                print(f'{k}: 1')
                beauty += 1
            else:
                print(f'{k}: 0')
                beauty += 0

        return beauty

