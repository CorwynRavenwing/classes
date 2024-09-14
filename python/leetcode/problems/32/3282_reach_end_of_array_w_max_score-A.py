class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:

        # given input index i, yield max possible score
        @cache
        def DP(i: int) -> int:
            print(f'DP({i})')

            # print(f'  [{i}]: scanning j in range({i+1},{len(nums)}):')
            answer = max(
                [
                    (j - i) * nums[i] + DP(j)
                    for j in range(i+1, len(nums))
                ],
                default=0
            )
            print(f'  [{i}]: {answer=}')
            return answer
        
        return DP(0)

# NOTE: works, but times out for large inputs
