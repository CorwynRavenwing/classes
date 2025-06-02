class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        def Triangle(X: int) -> int:
            # e.g. T(4) = 4+3+2+1 = 10 = (4 * 5 / 2)
            return X * (X + 1) // 2

        if 3 * limit < n:
            print(f'Cant divide {n=} among three piles under {limit=}')
            return 0

        minA = max(0, n - (2 * limit))
        maxA = min(n, limit)        
        print(f'A: {minA}..{maxA}')
        
        def get_minB_maxB_from_childA(childA: int) -> Tuple[int,int]:
            # print(f'\nGMMFCA({childA})')
            leftForBC = n - childA
            # print(f'  {childA=} {leftForBC=}')
            minB = leftForBC - limit    # again, B can't leave more than C can take
            # print(f'  {minB=} = {leftForBC=} - {limit=}')
            # again, no negative candies
            if minB < 0:
                # lower the maximum by however much below zero the minimum was
                maxB = limit + minB
                minB = 0
                # print(f'  < 0: new {(minB,maxB)=}')
            else:
                maxB = limit
                # print(f'  normal limit {maxB}')
            # print(f'{(minB, maxB)=}')
            return (minB, maxB)

        (minB_0, maxB_0) = get_minB_maxB_from_childA(minA)
        (minB_X, maxB_X) = get_minB_maxB_from_childA(maxA)

        if minB_0 == maxB_0:
            print(f'\nUsing Max version')
            (minB, maxB) = (minB_X, maxB_X)
        elif minB_X == maxB_X:
            print(f'\nUsing Min version')
            (minB, maxB) = (minB_0, maxB_0)
        else:
            print(f'\nUsing Manual version')
            answer = 0
            for childA in range(minA, maxA + 1):
                (minB, maxB) = get_minB_maxB_from_childA(childA)
                BC = maxB - minB + 1
                if answer < 1_000_000:
                    print(f'  child B/C {minB}..{maxB} ({BC})')
                answer += BC
            return answer

        BC = maxB - minB + 1
        print(f'  child B/C {minB}..{maxB} ({BC})')

        answer = Triangle(BC)
        
        return answer

# NOTE: Runtime 563 ms Beats 66.67%
# NOTE: Memory 16.65 MB Beats 8.70%

# NOTE: re-ran for challenge:
# NOTE: Runtime 547 ms Beats 35.62%
# NOTE: Memory 18.04 MB Beats 15.75%
