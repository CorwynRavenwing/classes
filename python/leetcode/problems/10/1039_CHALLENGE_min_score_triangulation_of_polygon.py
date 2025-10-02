class Solution:

    @cache
    def DP(self, values: List[int]) -> int:

        DEBUG = False

        if DEBUG: print(f'DP({values}): ?')

        def multiplyTriangle(values: Tuple[int,int,int]) -> int:
            (A, B, C) = values
            return A * B * C
        
        if len(values) == 3:
            answer = multiplyTriangle(values)
            if DEBUG: print(f'  -> {answer}')
            return answer
        if len(values) < 3:
            if DEBUG: print(f'  -> {0}')
            return 0
        
        answers = []
        N = len(values) - 1
        for K in range(1, N):
            triangle = (
                values[0],
                values[K],
                values[N]
            )
            if DEBUG: print(f'  {K=}: triangle({0},{K},{N}) = {triangle}')
            if DEBUG: print(f'    (subproblem [{0}..{K}]={values[:K+1]})')
            if DEBUG: print(f'    (subproblem [{K}..{N}]={values[K:]})')
            subproblems = [
                self.DP(values[:K+1]),
                multiplyTriangle(triangle),
                self.DP(values[K:]),
            ]
            if DEBUG: print(f'  {K=}: triangle({0},{K},{N}) = {triangle}: {subproblems[1]}')
            if DEBUG: print(f'    (subproblem [{0}..{K}]={values[:K+1]}): {subproblems[0]}')
            if DEBUG: print(f'    (subproblem [{K}..{N}]={values[K:]}): {subproblems[2]}')
            subproblem_sum = sum(subproblems)
            if DEBUG: print(f'  -> {subproblem_sum}')
            answers.append(subproblem_sum)
        if DEBUG: print(f'DP({values}): {answers=}')
        return min(answers)

    def minScoreTriangulation(self, values: List[int]) -> int:
        # make it hashable
        return self.DP(tuple(values))

# NOTE: Acceptance Rate 60.8% (medium)

# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 157 ms Beats 5.19%
# NOTE: Memory 21.84 MB Beats 10.77%

# NOTE: re-ran for challenge:
# NOTE: Runtime 155 ms Beats 5.28%
# NOTE: Memory 22.72 MB Beats 7.22%
