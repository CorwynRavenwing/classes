class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        prefixSum = (0,) + tuple(accumulate(stoneValue))
        # print(f'{prefixSum=}')

        def sum_of_range(L: int, R: int) -> int:
            # sum( stoneValue[L:R] )
            return prefixSum[R] - prefixSum[L]
        
        @cache
        def DP(L: int, R: int) -> int:
            # calculates the best score for range[L:R]
            # print(f'[{L}:{R}]')
            if R - L <= 1:
                # print(f'    DONE')
                return 0
            answers = []
            for M in range(L + 1, R):
                # print(f'  [{L}:{M}:{R}]')
                left = sum_of_range(L, M)
                right = sum_of_range(M, R)
                # print(f'  ({left},{right})')
                # print(f'  {left=}  {stoneValue[L:M]}')
                # print(f'  {right=} {stoneValue[M:R]}')
                if left <= right:
                    # print(f'    [try left]')
                    answers.append(
                        left + DP(L, M)
                    )
                if left >= right:
                    # print(f'    [try right]')
                    answers.append(
                        right + DP(M, R)
                    )
            answer = max(answers, default=0)
            # print(f'[{L}:{R}]: {answer} <- {answers}')
            return answer

        return DP(0, len(stoneValue))

# NOTE: Acceptance Rate 43.4% (HARD)

# NOTE: incomplete, TLE even with cache
