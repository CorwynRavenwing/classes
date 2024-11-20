class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        
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

        # @cache
        # nope.  we need to roll our own cache, excluding "depth"
        CFFPP_cache = {}
        def composite_factors_from_prime_power(Prime: int, Power: int, depth=0) -> Set[int]:
            cache_index = (Prime, Power)
            if cache_index in CFFPP_cache:
                return CFFPP_cache[cache_index]
            margin = '  ' * depth
            # print(f'{margin}CFFPP({Prime},{Power})')
            answer = {1}
            if Power == 0:
                # print(f'{margin}  {answer=}')
                CFFPP_cache[cache_index] = answer
                return answer
            CFFPP = composite_factors_from_prime_power(Prime, Power - 1, depth+1)
            answer = CFFPP | {
                A * Prime
                for A in CFFPP
            }
            # print(f'{margin}  {answer=}')
            CFFPP_cache[cache_index] = answer
            return answer

        # @cache
        def composite_factors_from_primes(Primes: List[int], depth=0) -> Set[int]:
            margin = '  ' * depth
            # print(f'{margin}CFFP({Primes})')
            answer = {1}
            if not Primes:
                # print(f'{margin}  {answer=}')
                return answer

            counts = Counter(Primes)
            # print(f'{margin}  {counts=}')

            for Prime, Count in counts.items():
                # print(f'{margin}  {Prime=} {Count=}')
                prime_powers = composite_factors_from_prime_power(Prime, Count, depth+1)
                # print(f'{margin}    {prime_powers=}')
                answer = {
                    A * B
                    for A in answer
                    for B in prime_powers
                }
                # print(f'{margin}    {answer=}')

            return answer

        @cache
        def factors_of(N: int) -> Set[int]:
            # print(f'factors_of({N})')

            F = factor(N)
            # print(f'  {F=}')
            CF = composite_factors_from_primes(F)

            return CF

        def factor_pairs_of(N: int) -> List[Tuple[int,int]]:
            answers = [
                (D, N // D)
                for D in factors_of(N)
            ]
            return sorted(answers)

        all_pairs = factor_pairs_of(num + 1) + factor_pairs_of(num + 2)
        BY_ABSOLUTE_DIFFERENCE = lambda X: abs(X[0] - X[1])
        all_pairs.sort(
            key=BY_ABSOLUTE_DIFFERENCE
        )
        print(f'{all_pairs=}')

        return all_pairs[0]

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Time Limit Exceeded)
# NOTE: Runtime 68 ms Beats 77.19%
# NOTE: Memory 17.44 MB Beats 5.41%
