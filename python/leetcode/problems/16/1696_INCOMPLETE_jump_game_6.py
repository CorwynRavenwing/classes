class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        # default to "always move 1":
        max_value_at_index = list(itertools.accumulate(nums))
        # print(f'{max_value_at_index=}')
        for i in range(0, len(nums) - 1):
            MaxAtI = max_value_at_index[i]
            print(f'check {i=} {MaxAtI}')
            for j in range(1, min(len(nums) - i, k + 1)):
                scoreAtJ = MaxAtI + nums[i + j]
                # print(f'  jump {j} to {i+j}: {scoreAtJ}')
                if max_value_at_index[i + j] < scoreAtJ:
                    max_value_at_index[i + j] = scoreAtJ
                    # print(f'  +{j}={i+j}: {scoreAtJ} (max)')
                    # print(f'{max_value_at_index=}')
        return max_value_at_index[-1]
# NOTE: Time Limit Exceeded for large inputs
