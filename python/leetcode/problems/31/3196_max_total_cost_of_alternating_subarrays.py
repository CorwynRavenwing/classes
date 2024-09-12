class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:

        @cache
        def DP(index: int, positive: bool) -> int:
            # print(f'{index}:DP({index},{positive})')
            if index >= len(nums):
                return 0
            N = nums[index]
            if positive:
                answer = N + DP(index + 1, False)
                # print(f'{index}:    either={answer}')
                return answer
            else:
                continue_this_subarray = -N + DP(index + 1, True)
                # print(f'{index}:    merge={continue_this_subarray}')
                start_new_subarray = N + DP(index + 1, False)
                # print(f'{index}:    split={start_new_subarray}')
                return max(continue_this_subarray, start_new_subarray)

        return DP(0, True)

# NOTE: Runtime 909 ms Beats 18.21%
# NOTE: Memory 288.12 MB Beats 5.56%
