class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        L = R = 0
        answer = 0
        Sum = 0

        while L <= R <= len(nums):
            score = Sum * (R - L)
            # print(f'[{L}:{R}] {Sum=} {score=} A={answer}')

            if score < k:
                if L < R:
                    additional = R - L
                    # print(f'  Yes: +{additional} (R-L = {R} - {L})')
                    answer += additional
                # print(f'  Yes: Expand right')
                try:
                    Sum += nums[R]
                except IndexError:
                    # print(f'  Fail OOB')
                    break
                R += 1
            else:
                # print(f'  No:  Shrink left')
                Sum -= nums[L]
                L += 1

        return answer

# NOTE: Acceptance Rate 62.5% (HARD)

# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 147 ms Beats 20.05%
# NOTE: Memory 30.60 MB Beats 43.13%

# NOTE: re-ran for challenge:
# NOTE: Runtime 159 ms Beats 15.91%
# NOTE: Memory 30.68 MB Beats 29.25%
