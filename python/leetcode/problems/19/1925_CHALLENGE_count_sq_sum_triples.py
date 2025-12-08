class Solution:
    def countTriples(self, n: int) -> int:
        
        C_squares = {
            C * C
            for C in range(1, n + 1)
        }
        # print(f'{C_squares=}')

        answer = 0
        for A in range(1, n + 1):
            for B in range(1, n + 1):
                C2 = A * A + B * B
                if C2 in C_squares:
                    print(f'{A},{B},{C2}')
                    answer += 1
                # else:
                #     print(f'{A},{B} -> {C2} not a square')
        
        return answer

# NOTE: Acceptance Rate 70.3% (easy)

# NOTE: Accepted on third Run (variable-name typos)
# NOTE: Accepted on first Submit
# NOTE: Runtime 115 ms Beats 79.08%
# NOTE: Memory 17.71 MB Beats 54.08%
