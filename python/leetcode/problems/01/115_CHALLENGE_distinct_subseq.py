class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        S = len(s)
        T = len(t)
        
        # @cache
        def DP_take(i: int, j: int) -> int:
            # print(f'DP_take({i},{j})')
            A = s[i]
            B = t[j]
            if A != B:
                # print(f'  NO: {A=} {B=}')
                return None
            
            return DP(i + 1, j + 1)

        # @cache
        def DP_skip(i: int, j: int) -> int:
            return DP(i + 1, j)

        @cache
        def DP(i: int, j: int) -> int:
            # print(f'DP({i}/{S},{j}/{T})')
            # check if we've run out of each string:
            try:
                A = s[i]
            except IndexError:
                A = None
            try:
                B = t[j]
            except IndexError:
                B = None
            
            if B is None:
                # print(f'YES: out of T')
                return 1

            if A is None:
                # print(f' NO: out of S')
                return None

            answers = [
                DP_take(i, j),
                DP_skip(i, j),
            ]
            while None in answers:
                answers.remove(None)

            if not answers:
                return None
            
            return sum(answers)
        
        answer = DP(0,0)
        if answer is None:
            return 0
        else:
            return answer

# NOTE: Acceptance Rate 52.5% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on fourth Submit (edge case; Output [add cache]; Output [delete prints])
# NOTE: Runtime 1086 ms Beats 5.00%
# NOTE: Memory 234.36 MB Beats 7.83%
