class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:

        mod = 10 ** 9 + 7
        
        diff = abs(startPos - endPos)
        print(f'{diff=}')

        if (diff % 2) != (k % 2):
            print(f'Wrong parity')
            return 0
        
        if diff > k:
            print(f'Too far apart')
            return 0
        
        k -= diff
        movesL = k // 2
        movesR = k // 2
        if startPos < endPos:
            movesR += diff
        else:
            movesL += diff
        print(f'Need {movesL} Left and {movesR} Right, in some order')

        @cache
        def Splunge(L: int, R: int, depth=0) -> int:
            margin = '  ' * depth
            if L > R:
                print(f'{margin}--swap {L},{R}--')
                return Splunge(R, L)
            print(f'{margin}Splunge({L},{R})')
            # Whatever Kind Of Combination That Is
            if L == 0 or R == 0:
                return 1
            else:
                # either pick a L and do this fn with the rest,
                # or pick a R and do this fn with the rest.
                return Splunge(L - 1, R) + Splunge(L, R - 1)
            
        return Splunge(movesL, movesR) % mod
# NOTE: Runtime 638 ms Beats 52.26%
# NOTE: Memory 168.20 MB Beats 41.98%
