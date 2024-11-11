class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        # these two functions are from IterTools Recipes:
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

        primesUnder1000 = tuple(sieve(1000))
        # print(f'{primesUnder1000=}')

        priorNum = 0
        for i, N in enumerate(nums):
            if N <= priorNum:
                print(f'No: {N=} <= {priorNum}')
                return False

            # we want N - prime > priorNum
            # -prime > -N + priorNum
            # prime < N - priorNum
            # prime <= N - priorNum - 1
            maxPrime = N - priorNum - 1
            # print(f'Search for {maxPrime=} = {N} - {priorNum} - 1')
            primeIndex = bisect_right(primesUnder1000, maxPrime) - 1
            if primeIndex < 0:
                print(f'No prime <= {maxPrime} available')
                priorNum = N
                continue

            prime = primesUnder1000[primeIndex]
            print(f'Found prime #{primeIndex} = {prime} <= {maxPrime}')
            print(f'  [{i}] {N} -> {N - prime}')
            N -= prime
            nums[i] = N
            if N <= priorNum:
                print(f'No: New {N=} is <= {priorNum}')
                return False
            priorNum = N
        print(f'after: {nums=}')
        
        return True
# NOTE: Runtime 127 ms Beats 65.26%
# NOTE: Memory 17.11 MB Beats 5.26%
# NOTE: re-ran for challenge and received:
# NOTE: Runtime 51 ms Beats 46.37%
# NOTE: Memory 17.27 MB Beats 5.34%
