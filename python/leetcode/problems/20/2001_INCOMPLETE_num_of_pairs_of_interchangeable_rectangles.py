class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:

        def AdividesB(A: int, B: int) -> bool:
            return (B % A == 0)
        
        @cache
        def factorsOf(N: int) -> Set[int]:
            # returns each factor only once, not including "1"
            orig_N = N
            if N == 1:
                answer = set()
                # print(f'FO({N}) returning {answer}')
                return answer
            print(f'factorsOf({orig_N})')
            if AdividesB(2, N):
                # print(f'  factor {2}')
                while AdividesB(2, N):
                    N //= 2
                answer = factorsOf(N)
                # print(f'FO({orig_N}) returning {2}: {answer}')
                return answer | {2}
            F = 3
            # print(f'FO({orig_N}) in-process: {answer}')
            while F <= N:
                if AdividesB(F, N):
                    # print(f'  factor {F}')
                    while AdividesB(F, N):
                        N //= F
                    answer = factorsOf(N)
                    # print(f'FO({orig_N}) returning {F}: {answer}')
                    return answer | {F}
                F += 2
            if N == 1:
                return set()
            # print(f'  factor {N} itself')
            return {N}

        def normalizeFraction(frac: Tuple[int,int]) -> Tuple[int,int]:
            frac = tuple(frac)
            (N, D) = frac
            # print(f'NF({frac}):')
            if N == 1 or D == 1:
                return frac
            fN = factorsOf(N)
            # print(f'  F({N}):{fN}')
            fD = factorsOf(D)
            # print(f'  F({D}):{fD}')
            fBoth = fN & fD     # "&": intersection
            # print(f'  shared factors {fBoth}')
            for F in fBoth:
                while AdividesB(F, N) and AdividesB(F, D):
                    N //= F
                    D //= F
                    frac = (N, D)
                    # print(f'  Divide {F} -> {frac}')
                if N == 1 or D == 1:
                    return frac
            return frac
        
        def Triangle(X: int) -> int: 
            return (X) * (X + 1) // 2

        normalized = [
            normalizeFraction(R)
            for R in rectangles
        ]
        print(f'{normalized=}')

        counts = Counter(normalized)
        print(f'{counts=}')

        answer = 0
        for (frac, count) in counts.items():
            pairs = Triangle(count - 1)
            # print(f'{frac=} {count=} {pairs=}')
            answer += pairs

        return answer
# NOTE: TLE for large inputs
