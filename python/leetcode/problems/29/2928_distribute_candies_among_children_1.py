class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        if 3 * limit < n:
            print(f'too many candies for 3 piles of {limit}')
            return 0

        minA = max(0, n - (2 * limit))
        maxA = min(n, limit)

        print(f'A: {minA}..{maxA}')
        answer = 0
        for childA in range(minA, maxA + 1):
            leftForBC = n - childA
            print(f'{childA=} {leftForBC=}')
            minB = leftForBC - limit    # again, B can't leave more than C can take
            # again, no negative candies
            if minB < 0:
                # lower the maximum by however much below zero the minimum was
                maxB = limit + minB
                minB = 0
            else:
                maxB = limit

            # for childB in range(minB, maxB + 1):
            #     childC = leftForBC - childB
            #     print(f'  {childB=} {childC=}')
            #     if childC > limit:
            #         print(f'    ERROR: {childC=} > {limit=}')
            #         continue
            #     if childC < 0:
            #         print(f'    less than zero')
            #         continue
            #     answer += 1
            # no need to loop through each answer: grab the entire B/C group at once
            BC = maxB - minB + 1
            print(f'  child B/C {minB}..{maxB} ({BC})')
            answer += BC
        
        return answer

# NOTE: 3-loops (commented out) version:
# NOTE: Runtime 126 ms Beats 42.08%
# NOTE: Memory 16.50 MB Beats 30.31%

# NOTE: Single-subtraction (entire B/C group) version:
# NOTE: Runtime 47 ms Beats 82.24%
# NOTE: Memory 16.49 MB Beats 70.46%

# NOTE: ... or, about twice as good in both parameters :-)
