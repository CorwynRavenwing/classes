class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        
        # we borrow some code from #1552:
        
        start.sort()

        def canFitNumbersAtTargetDistance(target: int) -> bool:
            # print(f'TEST({target}):')
            nonlocal start
            nonlocal d

            number = None
            for interval_start in start:
                interval_end = interval_start + d
                # print(f'  [{interval_start},{interval_end}]:')
                if number is None:
                    number = interval_start
                    # print(f'    first: {number}')
                else:
                    number += target
                    if number > interval_end:
                        # print(f'    FAIL:  {number}')
                        return False
                    if number < interval_start:
                        number = interval_start
                        # print(f'    jump:  {number}')
                    # elif interval_start <= number <= interval_end:
                    #     # print(f'    next:  {number}')

            return True

        L = 0
        left = canFitNumbersAtTargetDistance(L)
        if not left:
            print(f'Strange, {L=} is false')
            return L
        R = max(start) + d - min(start) + 1
        right = canFitNumbersAtTargetDistance(R)
        if right:
            print(f'Strange, {R=} is true')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = canFitNumbersAtTargetDistance(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Left')
                (L, left) = (M, mid)
            else:
                print(f'  False: replace Right')
                (R, right) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # L is now the highest possible True value
        return L

# NOTE: Runtime 1547 ms Beats 98.52%
# NOTE: Memory 32.10 MB Beats 12.93%
