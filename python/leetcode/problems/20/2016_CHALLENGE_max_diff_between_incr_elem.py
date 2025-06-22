class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        max_answer = -1
        min_seen = float('+inf')
        for N in nums:
            if N < min_seen:
                min_seen = N
                print(f'  {N}: new min')
            elif N > min_seen:
                answer = N - min_seen
                print(f'  {N}: {answer=}')
                max_answer = max(answer, max_answer)
        return max_answer

# NOTE: Acceptance Rate 60.0% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 4 ms Beats 41.21%
# NOTE: Memory 17.86 MB Beats 59.91%
