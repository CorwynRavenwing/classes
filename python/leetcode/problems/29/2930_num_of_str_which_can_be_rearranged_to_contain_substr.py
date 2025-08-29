class Solution:
    def stringCount(self, n: int) -> int:
        
        mod = 10 ** 9 + 7

        @cache
        def DP(L: int, E: int, T: int, digits: int) -> int:
            # label = f'DP("{"L" * L}{"E" * E}{"T" * T}",{digits})'
            letters = 26

            total = 0
            if digits == 0:
                if L or E or T:
                    # print(f'{label}: 0')
                    return 0
                else:
                    # print(f'{label}: 1')
                    return 1

            # print(f'{label}')

            if L:
                answer = 1 * DP(L - 1, E, T, digits - 1)
                # print(f'{label}: L={answer}')
                total += answer
                letters -= 1

            if E:
                answer = 1 * DP(L, E - 1, T, digits - 1)
                # print(f'{label}: E={answer}')
                total += answer
                letters -= 1

            if T:
                answer = 1 * DP(L, E, T - 1, digits - 1)
                # print(f'{label}: T={answer}')
                total += answer
                letters -= 1

            answer = letters * DP(L, E, T, digits - 1)
            # print(f'{label}: ({letters}) ={answer}')
            total += answer

            return total % mod
        
        answer = DP(1, 2, 1, n)

        return answer % mod

# NOTE: Acceptance Rate 55.8% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 1790 ms Beats 13.12%
# NOTE: Memory 393.74 MB Beats 6.56%
