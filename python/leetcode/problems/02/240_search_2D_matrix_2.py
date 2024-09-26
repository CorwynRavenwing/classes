class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # we borrowed some code from #74, but the main difference between
        # version 1 and this one (that the right end of row X does *not*
        # need to be lower than the left end of row X+1) makes that code
        # basically useless.

        M = len(matrix)
        N = len(matrix[0])
        UpperRight = (0, N-1)
        LowerLeft = (M-1, 0)
        (X, Y) = UpperRight
        while True:
            value = matrix[X][Y]
            print(f'[{X},{Y}]: {value}')
            if value == target:
                print(f'  FOUND')
                return True
            elif value < target:
                print(f'  Less: down')
                X += 1
                if X >= M:
                    print(f'    NO: fell off bottom edge')
                    return False
                continue
            elif value > target:
                print(f'  Greater: left')
                Y -= 1
                if Y < 0:
                    print(f'    NO: fell off left edge')
                    return False
                continue

        raise Exception('Logic error: fell out of infinite loop')

# NOTE: could not reuse code from Version 1
# NOTE: Accepted on first Submit
# NOTE: Runtime 139 ms Beats 59.67%
# NOTE: Memory 23.00 MB Beats 10.56%
