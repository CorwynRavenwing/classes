class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        L = 0
        R = len(arr) - 1
        left = arr[L]
        right = arr[R]

        # not sure whether we should check "left" and "right" here

        while L + 1 < R:
            M = (L + R) // 2
            midL = arr[M-1]
            mid = arr[M]
            midR = arr[M+1]
            print(f'B [{M-1}..{M+1}] = ({midL},{mid},{midR})')
            if midL < mid and mid > midR:
                print(f'  found mountain')
                return M
            if midL < mid:
                print(f'  slope up')
                (L, left) = (M, mid)
                continue
            if mid > midR:
                print(f'  slope down')
                (R, right) = (M, mid)
                continue
            else:
                raise Exception(f'Invalid values around {M=}: ({midL},{mid},{midR})')
        
        print(f'Z [{L},{R}] = ({left},{right})')
        return -999

