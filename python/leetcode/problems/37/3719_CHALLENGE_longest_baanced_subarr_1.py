class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        
        max_answer = 0

        for i in range(len(nums)):
            answer = 0
            seen = set()
            unbalance = 0
            for j in range(i, len(nums)):
                B = nums[j]
                answer += 1
                # print(f'[{i},{j}]({B}):')
                if B in seen:
                    # print(f'  dup')
                    pass
                else:
                    seen.add(B)
                    parity = (B % 2)
                    unbalance += (+1 if parity else -1)
                    # print(f'  {B}%{parity} -> {unbalance}')
                if not unbalance:
                    # print(f'    {answer=}')
                    max_answer = max(answer, max_answer)

        return max_answer

# NOTE: Acceptance Rate 55.7% (medium)

# NOTE: Accepted on second Run (edge case)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 1151 ms Beats 71.79%
# NOTE: Memory 19.80 MB Beats 13.28%
