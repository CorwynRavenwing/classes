class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        mod = 10 ** 9 + 7

        powers2 = [
            2 ** N
            for N in range(22)
        ]
        print(f'{powers2=}')

        mealCount = Counter(deliciousness)
        # print(f'{mealCount=}')
        meals = sorted(mealCount.keys())
        # print(f'{meals=}')
        pairs = []
        M = meals[-1]   # === max
        for A in meals:
            print(f'{A=}')
            for P in powers2:
                print(f'  {P=}')
                if A > P:
                    # skip forward until a large enough power of 2
                    print(f'    A > P, skip')
                    continue
                B = P - A
                print(f'    {B=}')
                if A > B:
                    print(f'    A > B, skip')
                    continue
                if B > M:
                    print(f'    B > M, quit')
                    break
                if B in meals:
                    print(f'    add A,B')
                    pairs.append(
                        (A, B)
                    )
                else:
                    print(f'    B not in list')
        print(f'{pairs=}')
        return -77777
        answer = 0
        for (A, B) in pairs:
            print(f'({A},{B}):')
            aCount = mealCount[A]
            bCount = mealCount[B]
            if A == B:
                if aCount == 1:
                    print(f'  cant duplicate single numbers')
                else:
                    print(f'  +{aCount} choose {2}')
                    answer += (aCount) * (aCount - 1) // 2
            else:
                print(f'  + {aCount} * {bCount}')
                answer += aCount * bCount
        
        return answer % mod
# NOTE: Time Limit Exceeded for large inputs
