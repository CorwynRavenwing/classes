class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:

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

        # pass in factor objects, get one back
        @cache
        def LCM_F(A: List[int], B: List[int]) -> List[int]:
            # print(f'LCM_F({A},{B}):')
            countA = Counter(A)
            # print(f'  {countA=}')
            countB = Counter(B)
            # print(f'  {countB=}')
            countC = {
                key: max(countA[key], countB[key])
                for key in set(tuple(countA.keys()) + tuple(countB.keys()))
            }
            # print(f'->{countC=}')
            answer = tuple([
                key
                for key, count in sorted(countC.items())
                for _ in range(count)
            ])
            return answer

        @cache
        def number_from_factor(F: List[int]) -> int:
            return math.prod(F)

        @cache
        def LCM(A: int, B: int) -> int:
            return number_from_factor(
                LCM_F(
                    factor(A),
                    factor(B)
                )
            )

        def tryValue(value: int) -> bool:
            print(f'{value=} {divisor1=} {divisor2=}')
            divisibleBy1 = value // divisor1
            divisibleBy2 = value // divisor2
            divisibleByBoth = value // LCM(divisor1, divisor2)
            divisibleBy1only = divisibleBy1 - divisibleByBoth
            divisibleBy2only = divisibleBy2 - divisibleByBoth
            divisibleByNeither = sum([
                value,
                -divisibleBy1only,
                -divisibleBy2only,
                -divisibleByBoth,
            ])
            print(f'{value=} 1={divisibleBy1} 2={divisibleBy2}')
            print(f'  1only={divisibleBy1only} 2only={divisibleBy2only}')
            print(f'  both={divisibleByBoth} neither={divisibleByNeither}')
            if False:
                d1 = []
                d2 = []
                dB = []
                dN = []
                for i in range(1, value + 1):
                    div1 = (i % divisor1 == 0)
                    div2 = (i % divisor2 == 0)
                    if div1:
                        if div2:
                            dB.append(i)
                        else:
                            d1.append(i)
                    else:
                        if div2:
                            d2.append(i)
                        else:
                            dN.append(i)
                print(f'({len(d1)}) {d1=}')
                print(f'({len(d2)}) {d2=}')
                print(f'({len(dB)}) {dB=}')
                print(f'({len(dN)}) {dN=}')
            (UC1, UC2) = (uniqueCnt1, uniqueCnt2)
            UC1 -= divisibleBy2only
            UC2 -= divisibleBy1only
            UC1 = max(0, UC1)
            UC2 = max(0, UC2)
            if UC1 + UC2 <= divisibleByNeither:
                print(f'    YES: {UC1=} + {UC2=} <= {divisibleByNeither}')
                return True
            else:
                print(f'    NO: {UC1=} + {UC2=} > {divisibleByNeither}')
                return False

        # binary search once again
        L = uniqueCnt1 + uniqueCnt2     # at least the number of slots required
        left = tryValue(L)
        if left:
            print(f'FOUND {L=}')
            return L
        (R, right) = (L, left)
        while not right:
            # if R -> False, make that the new lower bound
            (L, left) = (R, right)
            R *= 2
            right = tryValue(R)
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = tryValue(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  worked, try a lower number')
                (R, right) = (M, mid)
            else:
                print(f'  didnt work, try a higher number')
                (L, left) = (M, mid)
        print(f'[{L},{R}] ({left},{right})')
        # at this point, R === lowest possible True value
        return R
# NOTE: Runtime 44 ms Beats 6.34%
# NOTE: Memory 17.05 MB Beats 11.62%
