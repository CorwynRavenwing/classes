class Solution:

    def sqrtI(self, N: int) -> int:
        return int(N ** 0.5)

    primeSet = None

    def initPrimeData(self) -> None:
        max_input = 10 ** 9
        max_prime = self.sqrtI(max_input) + 1
        print(f'{max_input=} {max_prime=}')

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
        
        self.primeSet = set(sieve(max_prime))
        print(f'Sieve initialized to {len(self.primeSet)} primes')
    
    def isPrime(self, N) -> bool:
        if self.primeSet is None:
            self.initPrimeData()
        return N in self.primeSet

    def nonSpecialCount(self, l: int, r: int) -> int:

        (L, R) = (l, r)     # more legible variable names

        # SHORTCUT:
        # (A) Prime numbers have 2 divisors, and therefore 1 proper divisor,
        #       and so are not special.
        # (B) Non-square composite numbers have an even number of divisors,
        #       and therefore an odd number of proper divisors, so are
        #       not special.
        # (C) Square numbers have an odd number of divisors, and therefore
        #       an even number of proper divisors, but this number is
        #       generally large.
        # (D) Squares of primes have exactly three divisors, and therefore
        #       two proper divisors, and so are special.
        # Therefore we are seeking prime numbers, whose squares are
        #   between R and L ... and inverting this count:
        # NonSpecial = R - L + 1 - Special
        
        sqrtL = self.sqrtI(L) - 1
        sqrtR = self.sqrtI(R) + 1
        print(f'{sqrtL=} {sqrtR=}')
        special = 0
        for X in range(sqrtL, sqrtR):
            X2 = X * X
            if not (L <= X2 <= R):
                print(f'{X=} {X2=} out of range')
                continue
            if self.isPrime(X):
                print(f'{X} is prime: {X2} is special')
                special += 1
        print(f'{special=}')
        nonSpecial = R - L + 1 - special
        print(f'{nonSpecial=}')
        return nonSpecial

# NOTE: Accepted on first Submit
# NOTE: Trying something new here, moving code that only needs to
#       be run once (not once per test) out of the solution and
#       into the class itself.
#       Conclusion: it runs once per solution anyways.
# NOTE: Runtime 669 ms Beats 38.79%
# NOTE: Memory 17.22 MB Beats 8.51%
