class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:

        answers = []
        sorted_nums_x_ago = []
        for j, N in enumerate(nums):
            if j < x:
                # print(f'{j=} too low')
                continue
            if j - x < 0:
                raise Exception(f'ERROR: {j - x=} < 0')
            bisect.insort(sorted_nums_x_ago, nums[j - x])
            # print(f'DEBUG: {N=} {sorted_nums_x_ago=}')
            i = bisect_left(sorted_nums_x_ago, N)
            # print(f'  bisect @ {i=}')
            if i >= len(sorted_nums_x_ago):
                # print(f'  {i=} overran array: --')
                i -= 1
                tries = sorted_nums_x_ago[i:i+1]     # just the last number
            elif i == 0:
                # print(f'  {i=} bottom of array: ==')
                tries = sorted_nums_x_ago[0:1]       # just the first number
            else:
                # print(f'  {i-1=} {i=}')
                tries = sorted_nums_x_ago[i-1:i+1]     # prior number and this one
            # print(f'  {N=} {tries=}')
            for T in tries:
                diff = abs(N - T)
                # print(f'    {diff=}')
                answers.append(diff)

        return min(answers)
# NOTE: Runtime 948 ms Beats 86.67%
# NOTE: Memory 32.61 MB Beats 26.67%
