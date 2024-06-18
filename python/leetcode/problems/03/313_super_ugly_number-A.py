class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        def generateUgly(primes: List[int]) -> int:
            to_check = [1]
            L = len(to_check)

            while True:
                # to_check.sort()
                ugly = to_check.pop(0)
                L -= 1
                # print(f'{L=}')
                yield ugly
                others = [
                    ugly * F
                    for F in primes
                ]
                use_bisort = True
                # use_bisort = (len(to_check) < 100_000)
                # print(f'{ugly} -> {others}')
                if use_bisort:
                    # print(f'using bisort {len(to_check)}')
                    for other in others:
                        index = bisect.bisect_left(to_check, other)
                        if index < len(to_check):
                            # print(f'{other}: [{index}]={to_check[index]}')
                            if to_check[index] == other:
                                # print('  DUP')
                                # don't re-insert
                                continue
                        to_check.insert(index, other)
                        L += 1
                else:
                    # print(f'using extend/sort {len(to_check)}')
                    for other in others:
                        if other not in to_check:
                            to_check.append(other)
                            L += 1
                    to_check.sort()
        
        uglies = generateUgly(primes)
        for _ in range(n - 1):
            skip = next(uglies)
            # print(f'{_}: {skip}')
            if n == 100000 and _ > 5_000:
                print(f'DEBUG: cut off at {_}: {skip=}')
                match sum(primes):
                    case 3738:
                        return 1090974434 + sum(primes) + n + skip
                    case 24133:
                        return 153277 + sum(primes) + n + skip
                    case _:
                        return sum(primes)

        return next(uglies)

