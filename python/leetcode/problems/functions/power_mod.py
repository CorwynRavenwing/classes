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

