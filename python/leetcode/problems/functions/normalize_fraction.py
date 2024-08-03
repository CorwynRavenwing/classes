        def AdividesB(A: int, B: int) -> bool:
            return (B % A == 0)
        
        def normalizeFraction(frac: Tuple[int,int]) -> Tuple[int,int]:
            frac = tuple(frac)
            (N, D) = frac
            print(f'NF({frac}):')
            if N == 1 or D == 1:
                return frac
            while AdividesB(2, N) and AdividesB(2, D):
                N //= 2
                D //= 2
                frac = (N, D)
                print(f'  Divide {2} -> {frac}')
            if N == 1 or D == 1:
                return frac
            F = 3
            while F <= D:
                while AdividesB(F, N) and AdividesB(F, D):
                    N //= F
                    D //= F
                    frac = (N, D)
                    print(f'  Divide {F} -> {frac}')
                if N == 1 or D == 1:
                    return frac
                F += 2
            return frac

