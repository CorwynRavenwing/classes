class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:

        # these three functions are from IterTools Recipes:
        # https://docs.python.org/3/library/itertools.html

        import contextlib

        def iter_index(iterable, value, start=0, stop=None):
            "Return indices where a value occurs in a sequence or iterable."
            # iter_index('AABCADEAF', 'A') → 0 1 4 7
            seq_index = getattr(iterable, 'index', None)
            if seq_index is None:
                iterator = islice(iterable, start, stop)
                for i, element in enumerate(iterator, start):
                    if element is value or element == value:
                        yield i
            else:
                stop = len(iterable) if stop is None else stop
                i = start
                with contextlib.suppress(ValueError):
                    while True:
                        yield (i := seq_index(value, i, stop))
                        i += 1

        def sieve(n):
            "Primes less than n."
            # sieve(30) → 2 3 5 7 11 13 17 19 23 29
            if n > 2:
                yield 2
            data = bytearray((0, 1)) * (n // 2)
            for p in iter_index(data, 1, start=3, stop=math.isqrt(n) + 1):
                data[p*p : n : p+p] = bytes(len(range(p*p, n, p+p)))
            yield from iter_index(data, 1, start=3)

        def factor(n):
            "Prime factors of n."
            # factor(99) → 3 3 11
            # factor(1_000_000_000_000_007) → 47 59 360620266859
            # factor(1_000_000_000_000_403) → 1000000000000403
            for prime in sieve(math.isqrt(n) + 1):
                while not n % prime:
                    yield prime
                    n //= prime
                    if n == 1:
                        return
            if n > 1:
                yield n
                
        def AdividesB(A: int, B: int) -> bool:
            return (B % A == 0)

        @cache
        def normalizeFraction(frac: Tuple[int,int]) -> Tuple[int,int]:
            frac = tuple(frac)
            (N, D) = frac
            print(f'NF({frac}):')
            if N == 1 or D == 1:
                return frac
            for F in factor(N):
                while AdividesB(F, N) and AdividesB(F, D):
                    N //= F
                    D //= F
                    frac = (N, D)
                    print(f'  Divide {F} -> {frac}')
                if N == 1 or D == 1:
                    return frac
            return frac

        stockPrices.sort()
        # print(f'{stockPrices=}')
        differences = [
            (X2 - X1, Y2 - Y1)
            for ((X1, Y1), (X2, Y2)) in zip(stockPrices, stockPrices[1:])
        ]
        # print(f'{differences=}')
        normalized_differences_with_count = [
            (normalizeFraction(slope), 1)
            for slope in differences
        ]
        # print(f'{normalized_differences_with_count=}')
        for i in range(1, len(normalized_differences_with_count)):
            (thisDiff, thisCount) = normalized_differences_with_count[i]
            (prevDiff, prevCount) = normalized_differences_with_count[i - 1]
            if thisDiff == prevDiff:
                # print(f'merge {i-1} and {i} ({thisDiff}: {thisCount} + {prevCount})')
                normalized_differences_with_count[i] = (thisDiff, thisCount + prevCount)
                normalized_differences_with_count[i - 1] = None
        while None in normalized_differences_with_count:
            normalized_differences_with_count.remove(None)
        print(f'merged {normalized_differences_with_count=}')
        
        return len(normalized_differences_with_count)

