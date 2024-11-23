class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
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

        def factor_cacheme(n):
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

        @cache
        def factor(n):
            return tuple(factor_cacheme(n))

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

        answer = set()
        for Divisor in range(1, n + 1):
            for Numerator in range(1, Divisor):
                fraction = (Numerator, Divisor)
                normalized = normalizeFraction(fraction)
                # print(f'{fraction=} {normalized=}')
                if fraction == normalized:
                    answer.add(f'{Numerator}/{Divisor}')

        return tuple(answer)

# NOTE: Accepted on second Run (output format mismatch)
# NOTE: Accepted on first Submit
# NOTE: Runtime 305 ms Beats 17.69%
# NOTE: Memory 18.46 MB Beats 5.79%
