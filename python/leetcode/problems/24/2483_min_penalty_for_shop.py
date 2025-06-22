class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        match = lambda char: tuple([(1 if C == char else 0) for C in customers])
        Y = match('Y')
        N = match('N')
        # print(f'{N=}')
        # print(f'{Y=}')

        ACC = lambda L: (0,) + tuple(accumulate(L))
        REV = lambda L: tuple(reversed(L))
        RACC = lambda L: REV(ACC(REV(L)))
        prefix_N = ACC(N)
        suffix_Y = RACC(Y)
        # print(f'{prefix_N=}')
        # print(f'{suffix_Y=}')

        penalties = tuple(map(sum, zip(prefix_N, suffix_Y)))
        # print(f'{penalties=}')
        min_penalty = min(penalties)
        answer = penalties.index(min_penalty)
        print(f'[{answer}] {min_penalty=}')

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 159 ms Beats 28.40%
# NOTE: Memory 31.66 MB Beats 5.07%
