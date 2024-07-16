class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:

        ApplePile = Counter()
        eaten = 0
        for (day, A, D) in zip(range(1, len(apples) + 1), apples, days):
            expireDay = day + D
            if D:
                # print(f'{day}: +{A}')
                ApplePile[expireDay] += A
            # else:
            #     print(f'{day}: +0')
            expired = ApplePile[day]
            if expired:
                # print(f'  x{expired}')
                del ApplePile[day]
            (eatD, eatA) = min(
                [(pD, pA) for (pD, pA) in ApplePile.items()],
                default = (0,0)
            )
            if eatA:
                # print(f'  -1')
                eaten += 1
                ApplePile[eatD] -= 1
                if not ApplePile[eatD]:
                    # print(f'    =0')
                    del ApplePile[eatD]
            # else:
            #     print(f'  -0')
        print(f'--- apples stop ---')
        appleBarrel = [(pD, pA) for (pD, pA) in ApplePile.items()]
        appleBarrel.sort()
        day += 1
        while appleBarrel:
            print(f'{day}:')
            (eatD, eatA) = appleBarrel.pop(0)
            print(f'  {(eatD, eatA)}')
            if eatD <= day:
                print(f'  x{expired}')
                # Do not increment day here!
                continue
            if eatA:
                days_eating_these = min(eatA, eatD - day)
                print(f'  -{days_eating_these}')
                day += days_eating_these
                eaten += days_eating_these
                eatA -= days_eating_these
                if eatA:
                    print(f'  x{eatA}')
            else:
                print(f'  -0')
                day += 1
        print(f'{day}: stop')
        return eaten
# NOTE: gives Time Limit Exceeded for large inputs
