class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:

        # return [
        #     i
        #     for i, (aI, bI, cI, mI) in enumerate(variables)
        #     if (
        #         ((((aI ** bI) % 10) ** cI) % mI) == target
        #     )
        # ]

        def power_mod(base: int, power: int, mod: int) -> int:
            print(f'power_mod({base},{power},{mod}):')
            if power > 10:
                # A^((B*C) + D) == A^(B*C) * A^D == (A^B)^C * A^D
                A = base
                B = 10
                C = power // 10
                D = power % 10
                print(f'  {A=} {B=} {C=} {D=}')
                AtoB = power_mod(A, B, mod)
                AtoBC = power_mod(AtoB, C, mod)
                AtoD = power_mod(A, D, mod)
                answer = AtoBC * AtoD
                print(f'  A^B={AtoB}, ^C={AtoBC}, A^D={AtoD}')
                return answer % mod
            else:
                print(f'  simple')
                return (base ** power) % mod

        return [
            i
            for i, (aI, bI, cI, mI) in enumerate(variables)
            if (
                power_mod(
                    power_mod(aI, bI, 10),
                    cI,
                    mI
                ) == target
            )
        ]

# NOTE: Accepted on first Submit

# NOTE: brute-force solution:
# NOTE: Runtime 65 ms Beats 19.09%
# NOTE: Memory 16.66 MB Beats 48.96%

# NOTE: solution using power_mod:
# NOTE: Runtime 72 ms Beats 6.40%
# NOTE: Memory 16.94 MB Beats 23.60%
# NOTE: approximately the same speed and memory
