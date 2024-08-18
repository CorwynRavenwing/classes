class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        grid_H = len(points)
        grid_W = len(points[0])

        MAX = lambda x: tuple(accumulate(tuple(x), max))
        REV = lambda x: tuple(reversed(tuple(x)))

        firstRow = points[0]
        otherRows = points[1:]
        print(f'  row={firstRow[:5]}...{firstRow[-5:]}')
        DP = firstRow   # no penalties for row #0
        print(f'  DP={DP[:5]}...{DP[-5:]}')
        for row in otherRows:
            print(f'  row={row[:5]}...{row[-5:]}')
            LeftMaxPlus = MAX(
                [
                    data + b
                    for b, data in enumerate(DP)
                ]
            )
            # print(f'{LeftMaxPlus=}')
            RightMaxMinus = REV(MAX(REV(
                [
                    data - b
                    for b, data in enumerate(DP)
                ]
            )))
            # print(f'{RightMaxMinus=}')
            DP = [
                value + max([
                    LeftMaxPlus[j] - j,
                    RightMaxMinus[j] + j
                ])
                for j, value in enumerate(row)
            ]
            print(f'  DP={DP[:5]}...{DP[-5:]}')

        return max(DP)
# NOTE: Runtime 1855 ms Beats 7.40%
# NOTE: Memory 50.81 MB Beats 51.85%
