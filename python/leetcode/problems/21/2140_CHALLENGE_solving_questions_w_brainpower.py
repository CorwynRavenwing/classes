class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        def dp_skip(q: int) -> int:
            # (points, brainpower) = questions[q]
            return dp(q + 1)
        
        def dp_take(q: int) -> int:
            (points, brainpower) = questions[q]
            return points + dp(q + 1 + brainpower)
        
        @cache
        def dp(q: int) -> int:
            try:
                check = questions[q]
            except IndexError:
                return 0
            return max([
                dp_skip(q),
                dp_take(q),
            ])
        
        return dp(0)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Time Exceeded: add cache)
# NOTE: Runtime 307 ms Beats 5.01%
# NOTE: Memory 141.56 MB Beats 5.44%

# NOTE: re-ran for challenge:
# NOTE: Runtime 293 ms Beats 5.29%
# NOTE: Memory 141.83 MB Beats 5.72%
