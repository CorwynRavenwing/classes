class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        JOIN = lambda L: ''.join(L)

        ADDMOD_A_RAW = lambda X: str((int(X) + a) % 10)
        ADDMOD_A_ODD = lambda i, C: (ADDMOD_A_RAW(C) if i % 2 == 1 else C)
        OP1_raw = lambda L: [ADDMOD_A_ODD(i, C) for i, C in enumerate(L)]
        OP1 = lambda X: JOIN(OP1_raw(X))

        CYCLE_B = lambda L: (L[-b:] + L[:-b])
        OP2 = lambda X: CYCLE_B(X)

        min_answer = s
        seen = set()
        queue = {s}
        while queue:
            answer = queue.pop()
            if answer in seen:
                # print(f'{min_answer}: {answer} (seen)')
                continue
            else:
                seen.add(answer)
            min_answer = min(answer, min_answer)
            op1 = OP1(answer)
            op2 = OP2(answer)
            # print(f'{min_answer}: {answer} -> {op1} {op2}')
            queue.add(op1)
            queue.add(op2)
        
        return min_answer

# NOTE: Acceptance Rate 66.2% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 1017 ms Beats 18.42%
# NOTE: Memory 18.88 MB Beats 55.33%

# NOTE: re-ran for challenge:
# NOTE: Runtime 1019 ms Beats 17.27%
# NOTE: Memory 19.40 MB Beats 74.82%
