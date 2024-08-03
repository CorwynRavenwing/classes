class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        answer = 0
        leftSum = 0
        rightCount = len(nums)
        targetSum = sum(nums) / 2
        
        for N in nums:
            leftSum += N
            rightCount -= 1
            # print(f'{N}: {leftSum} ({rightCount})')
            if rightCount == 0:
                print(f'  ran out of numbers on Right side')
            elif leftSum >= targetSum:
                # print(f'  Yes')
                answer += 1
            # else:
            #     print(f'  No')
        
        return answer
# NOTE: Runtime 672 ms Beats 62.56%
# NOTE: Memory 31.25 MB Beats 45.24%
