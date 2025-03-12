class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        # SHORTCUT: assume X, Y, and Z are primes, X < Y < Z.
        # (Z - X) === (Y - X) + (Z - Y)
        # each of these differences is a nonnegative number.
        # Therefore Z-X will be larger than either of the other two,
        # and can be ignored.  This means we only care about differences
        # between *pairs of adjacent* primes, rather than any other pairing.

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

        prior_prime = None
        best_diff = float('+inf')
        answer = [-1, -1]
        for prime in sieve(right + 1):
            if prime < left:
                # print(f'{prime=} (low)')
                continue
            if prior_prime is None:
                print(f'{prior_prime} {prime} (first) {answer=}')
                prior_prime = prime
                continue
            diff = prime - prior_prime
            if best_diff > diff:
                # strict ">" so we choose the lower pair when equal
                best_diff = diff
                answer = [prior_prime, prime]
            print(f'{prior_prime} {prime} {diff=} {answer=}')
            if diff == 2:
                print(f'  BEST POSSIBLE ANSWER')
                break
            prior_prime = prime
        
        return answer

# NOTE: Runtime 370 ms Beats 74.18%
# NOTE: Memory 18.77 MB Beats 70.59%

# NOTE: re-ran for challenge:
# NOTE: Runtime 319 ms Beats 62.81%
# NOTE: Memory 20.04 MB Beats 68.44%
