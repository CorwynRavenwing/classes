class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        # SECTION 1: PRIMES AND FACTORIZATION

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

        # SECTION 2: PRECALCULATE HELPER ARRAYS

        def prime_score(n: int) -> int:
            if n == 1:
                return 0
            F = factor(n)
            score = len(set(F))
            # print(f'{n}: {F} -> {score}')
            return score

        scores = [prime_score(N) for N in nums]
        # print(f'{scores=}')

        left = []
        queue = []
        not_found = -1
        for (index, score) in enumerate(scores):
            # print(f'{index}: {score}')
            left_index = not_found
            while queue:
                # print(f'  Q={queue}')
                (left_score, left_index) = queue[-1]
                # print(f'  left = {queue[-1]}')
                if left_score >= score:
                    # print(f'    {left_score} >= {score}')
                    break
                else:
                    # drop irrelevant, lower score
                    # print(f'    {left_score} < {score} POP')
                    _ = queue.pop(-1)
                    left_index = not_found
            left.append(left_index)
            queue.append(
                (score, index)
            )
            # print(f'  Q={queue}')
        # print(f'{left=}')

        right = []
        queue = []
        n = len(nums)
        not_found = n
        for (index, score) in reversed(tuple(enumerate(scores))):
            # print(f'{index}: {score}')
            right_index = not_found
            while queue:
                # print(f'  Q={queue}')
                (right_score, right_index) = queue[-1]
                # print(f'  right = {queue[-1]}')
                if right_score > score:
                    # print(f'    {right_score} > {score}')
                    break
                else:
                    # drop irrelevant, lower score
                    # print(f'    {right_score} <= {score} POP')
                    _ = queue.pop(-1)
                    right_index = not_found
            right.append(right_index)
            queue.append(
                (score, index)
            )
            # print(f'  Q={queue}')
        right = list(reversed(right))
        # print(f'{right=}')

        ranges = [
            (i - L) * (R - i)
            for (i, L, R) in zip(itertools.count(), left, right)
        ]
        # print(f'{ranges=}')

        ordered_nums_ranges = list(zip(nums, ranges))
        ordered_nums_ranges.sort(reverse=True)
        # print(f'{ordered_nums_ranges=}')

        # SECTION 3: CALCULATE SCORE K TIMES

        mod = 10 ** 9 + 7
        answer = 1
        while k:
            # print(f'\n{k=} {answer=}')
            (Number, Ranges) = ordered_nums_ranges.pop(0)
            k_used = min(Ranges, k)
            # print(f'  {Number=} {Ranges=}({k_used})')
            update = pow(Number, k_used, mod)
            # print(f'    {update=}')
            answer *= update
            answer %= mod
            k -= k_used
        # print(f'\n{k=} {answer=}')
        return answer

# NOTE: Acceptance Rate 33.8% (HARD)

# NOTE: Accepted on third Run (*ERROR* IN HINTS!)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 4766 ms Beats 10.53%
# NOTE: Memory 45.87 MB Beats 32.46%
