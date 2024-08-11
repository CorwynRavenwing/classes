class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:

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

        mod = 10 ** 9 + 7

        factorizations = [
            factor(N)
            for N in nums
        ]
        print(f'raw {factorizations=}')
        factorizations = [
            F
            for F in factorizations
            if max(Counter(F).values(), default=1) == 1
        ]
        print(f'de-squared {factorizations=}')
        ones = len([
            1
            for F in factorizations
            if F == ()
        ])
        print(f'{ones=}')
        factorizations = [
            F
            for F in factorizations
            if F != ()
        ]
        print(f'no-ones {factorizations=}')
        factorCounts = Counter(factorizations)
        print(f'{factorCounts=}')
        factorKeys = tuple(sorted(factorCounts.keys()))
        print(f'{factorKeys=}')

        ones_factor = 2 ** ones
        answer = 0
        for i, KeyI in enumerate(factorKeys):
            count = factorCounts[KeyI]
            print(f'{i}: {KeyI} ({count})')
            thisGroupCount = count
            thisGroupPrimes = set(KeyI)
            print(f'  {thisGroupCount} * {ones_factor}')
            answer += thisGroupCount * ones_factor
            print(f'    = {thisGroupCount * ones_factor} (total {answer})')
            for j, KeyJ in enumerate(factorKeys):
                if j <= i:
                    continue
                count = factorCounts[KeyJ]
                print(f'  {j}: {KeyJ} ({count})')
                setJ = set(KeyJ)
                if thisGroupPrimes.intersection(setJ):
                    print(f'    Overlap {thisGroupPrimes},{setJ}')
                    continue
                thisGroupCount *= count
                thisGroupPrimes |= setJ
                print(f'  {thisGroupCount} * {ones_factor}')
                answer += thisGroupCount * ones_factor
                print(f'    = {thisGroupCount * ones_factor} (total {answer})')

        ones_alone = (2 ** ones) - 1    # b/c you can't have "zero ones", the empty set
        answer += ones_alone
        print(f'{ones_alone=} (total {answer})')

        return answer % mod

# NOTE: the code to this is incorrect, in that it only counts
# groups that are made up of greedily picking up all possible
# later primes, rather than also including *skipping* a prime.
# e.g. for primes 2, 3, 5, 7, it sees groups 2, 2,3, 2,3,5, and 2,3,5,7,
# but misses groups like 2,5 and 2,5,7.  It does find 3, 3,5, 3,5,7 because
# we are treating the first prime differently, but not e.g. 3,7
# I'm unsure how to fix this without causing combinatorial explosion.
# My thought is to make "pick unconnected primes" a recursive function,
# passing in "index to start at" and "other primes to not allow" as parameters.
# Hopefully memoizing this will handle the speed issue.

