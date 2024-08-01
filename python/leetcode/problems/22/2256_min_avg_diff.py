class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        leftCount = 0
        leftSum = 0
        rightCount = len(nums)
        rightSum = sum(nums)
        min_avg_diff = float('+inf')
        answer = -1
        print(f'ORIGINAL MINIMUM #{answer}: {min_avg_diff}')
        for i, N in enumerate(nums):
            # print(f'{i=} L=...{nums[max(0,i-1):i+1]} R={nums[i+1:i+3]}...')
            leftCount += 1
            leftSum += nums[i]
            rightCount -= 1
            rightSum -= N
            leftAvg = ((leftSum // leftCount) if leftCount else 0)
            rightAvg = ((rightSum // rightCount) if rightCount else 0)
            # print(f'  {leftSum}/{leftCount} <=> {rightSum}/{rightCount}')
            AvgDiff = abs(leftAvg - rightAvg)
            # print(f'    {leftAvg} <=> {rightAvg} = {AvgDiff}')
            if min_avg_diff > AvgDiff:
                min_avg_diff = AvgDiff
                answer = i
                print(f'NEW MINIMUM #{answer}: {min_avg_diff}')
                if min_avg_diff == 0:
                    print(f'  It is not going to get any lower')
                    break
        return answer
# NOTE: Runtime 581 ms Beats 100.00%    *** WOW ***
# NOTE: Memory 27.42 MB Beats 27.78%
