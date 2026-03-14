class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        
        def Triangle(N: int) -> int:
            return (N) * (N + 1) // 2

        def ReverseTriangle(S: int) -> int:
            # number whose triangle function "N*(N + 1)/2" is S:
            return int(math.sqrt(2 * S))

        def isPossible(target: int) -> bool:
            print(f'P({target}):')
            workShare = [
                target // workerTime + (1 if (target % workerTime) else 0)
                for workerTime in workerTimes
            ]
            print(f'  {workShare=}')
            Xn = [
                ReverseTriangle(work)
                for work in workShare
            ]
            print(f'  {Xn=}')
            removed = sum(Xn)
            print(f'  answer={removed >= mountainHeight}')
            return removed >= mountainHeight

        L = 0
        left = isPossible(L)
        if left:
            print(f'Strange, {L=} is true')
            return L
        R = Triangle(mountainHeight) + 1
        right = isPossible(R)
        if not right:
            print(f'Strange, {R=} is false')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = isPossible(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Right')
                (R, right) = (M, mid)
            else:
                print(f'  False: replace Left')
                (L, left) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # R is now the lowest possible True value
        return R

# NOTE: Acceptance Rate 39.4% (medium)

# NOTE: wrong answer
