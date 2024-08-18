class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        # we borrow some code from #2873
        # the exact code worked, but had Memory Limit Exceeded for large inputs

        REV = lambda x: tuple(reversed(tuple(x)))

        MAX = lambda x: tuple(accumulate(x, max))

        maxLeft = MAX(nums)
        maxRight = REV(MAX(REV(nums)))
        # print(f' {maxLeft=}')
        # print(f'{maxRight=}')

        values = [0] + [
            (maxLeft[j - 1] - nums[j]) * maxRight[j + 1]
            for j in range(1, len(nums)-1)
        ]
        # print(f'{values=}')
        return max(values)
# NOTE: Runtime 736 ms Beats 70.62%
# NOTE: Memory 30.30 MB Beats 31.75%
