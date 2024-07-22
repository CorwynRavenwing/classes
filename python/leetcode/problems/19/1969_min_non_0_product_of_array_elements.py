class Solution:
    def minNonZeroProduct(self, p: int) -> int:

        mod = 10 ** 9 + 7

        # NOTE: Former program is correct, but takes far too long to run.
        # Time Limit Exceeded for input "4" :-/
        
        # but it does show us the pattern of the right answer.
        # e.g. 3 -> 001 001 001 110 110 110 111 (1 1 1 6 6 6 7)
        # e.g. 4 -> 1^7 * 14^7 * 15
        # for P=4, M=(2^(P-1))=8, N=(2^P)=16, these numbers are:
        # 1^(M-1) * (N-2)^(M-1) * (N-1)
        # and this generalizes for all cases

        N = 2 ** p          # for p=4, this is 16
        M = 2 ** (p - 1)    # for p=4, this is 8, or N // 2

        # GroupOfMminus1Ones = [1] * (M - 1)
        # GroupOfMminus1Nminus2s = [N - 2] * (M - 1)
        # OneNminus1 = [N - 1]
        # answerArray = (
        #     GroupOfMminus1Ones + GroupOfMminus1Nminus2s + OneNminus1
        # )

        def power_mod(base: int, power: int) -> int:
            print(f'power_mod({base},{power}):')
            if power > 10:
                # A^((B*C) + D) == A^(B*C) * A^D == (A^B)^C * A^D
                A = base
                B = 10
                C = power // 10
                D = power % 10
                print(f'  {A=} {B=} {C=} {D=}')
                AtoB = power_mod(A, B)
                AtoBC = power_mod(AtoB, C)
                AtoD = power_mod(A, D)
                answer = AtoBC * AtoD
                print(f'  A^B={AtoB}, ^C={AtoBC}, A^D={AtoD}')
                return answer % mod
            else:
                print(f'  simple')
                return (base ** power) % mod

        print(f'answer array = {[1]}*{(M - 1)} + {[N - 2]}*{(M - 1)} +{[N - 1]}')
        # answer = 1 ** (M - 1) * (N - 2) ** (M - 1) * (N - 1)
        # answer = (N - 2) ** (M - 1) * (N - 1)
        answer = power_mod(N - 2, M - 1)
        answer *= (N - 1)
        return answer % mod

