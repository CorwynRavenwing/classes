class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:

        # instead of following Hint 1, I'm taking a different,
        # more straightforward tack.

        # 1) compute prefixMin and prefixMax from nums:
        prefixMin = tuple(accumulate(nums, min))
        prefixMax = tuple(accumulate(nums, max))

        for i in range(indexDifference, len(nums)):
            # 2) that turns Hint 2 into the following tests:
            minNums = prefixMin[i - indexDifference]
            diffFromMin = abs(nums[i] - minNums)
            if (diffFromMin >= valueDifference):
                minJ = nums.index(minNums)
                return [i, minJ]

            maxNums = prefixMax[i - indexDifference]
            diffFromMax = abs(nums[i] - maxNums)
            if (diffFromMax >= valueDifference):
                maxJ = nums.index(maxNums)
                return [i, maxJ]

        return [-1, -1]

# NOTE: Accepted first Submit
# NOTE: Runtime 608 ms Beats 30.50%
# NOTE: Memory 31.45 MB Beats 60.28%
