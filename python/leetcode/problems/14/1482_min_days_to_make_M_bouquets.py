class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        # minimum of something monotomically increasing ==> binary search

        def canMakeMbouquetsOnTargetDay(target: int) -> bool:
            # print(f'-->{target=}')
            flowers = [
                (
                    'Y'
                    if (target >= D)
                    else ' '
                )
                for D in bloomDay
            ]
            # print(f'-->{flowers=}')
            counts = [
                (key, len(tuple(values)))
                for key, values in groupby(flowers)
            ]
            print(f'{counts=}')
            needed = m
            while needed and counts:
                (letter, count) = counts.pop(0)
                if letter == ' ':
                    continue
                bouquets = count // k
                # print(f'-->{count}:{bouquets}')
                needed -= min(bouquets, needed)
            
            if needed:
                # print(f'-->{needed=} leftover')
                return False
            else:
                return True

        L = 0
        left = canMakeMbouquetsOnTargetDay(L)
        if left:
            print(f'Strange, {L=} is true')
            return L
        R = max(bloomDay) + 1
        right = canMakeMbouquetsOnTargetDay(R)
        if not right:
            print(f'Strange, {R=} is false')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = canMakeMbouquetsOnTargetDay(M)
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

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 1919 ms Beats 5.04%
# NOTE: Memory 36.22 MB Beats 5.51%
