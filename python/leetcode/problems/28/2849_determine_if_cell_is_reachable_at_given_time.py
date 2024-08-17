class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        distance = max([
            abs(sx - fx),
            abs(sy - fy),
        ])
        if distance > t:
            print(f'NO: Too far away')
            return False
        elif distance == 0:
            print(f'We are already there')
            if t == 1:
                print(f'  NO: have to move away, no time to return')
                return False
        #     elif t == 0:
        #         print(f'  YES: {t=}')
        #         return True
        #     else:
        #         print(f'  YES: move away and move back')
        #         return True
        # elif distance == t:
        #     print(f'YES: exactly enough time')
        #     return True
        # else:
        #     print(f'YES: move there, circle around until time elapses')
        #     return True
        return True
# NOTE: Runtime 41 ms Beats 26.85%
# NOTE: Memory 16.52 MB Beats 37.04%
