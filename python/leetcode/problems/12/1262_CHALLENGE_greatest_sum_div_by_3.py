class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        def DP_pick(index: int, mod: int) -> int:
            N = nums[index]
            answer = DP(
                index + 1,
                (mod + N) % 3
            )
            if answer is None:
                return None
            else:
                return N + answer

        def DP_skip(index: int, mod: int) -> int:
            N = nums[index]
            return DP(
                index + 1,
                mod
            )
        
        @cache
        def DP(index: int, mod: int) -> int:
            print(f'DP({index},%{mod})')
            try:
                _ = nums[index]
            except IndexError:
                if mod == 0:
                    return 0
                else:
                    return None
            answers = [
                DP_pick(index, mod),
                DP_skip(index, mod),
            ]
            while None in answers:
                answers.remove(None)
            return max(answers, default=None)
        
        answer = DP(0, 0)
        if answer is None:
            return 0
        else:
            return answer

# NOTE: Acceptance Rate 51.3% (medium)

# NOTE: re-created for challenge
# NOTE: Accepted on third Run (edge cases with no answer)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 751 ms Beats 5.03%
# NOTE: Memory 143.34 MB Beats 6.80%
