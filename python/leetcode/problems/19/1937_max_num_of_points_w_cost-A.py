class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        grid_H = len(points)
        grid_W = len(points[0])

        @cache
        def penalties(oldC: int) -> List[int]:
            # print(f'Computing penalties({oldC})')
            return [
                - abs(oldC - newC)
                for newC in range(grid_W)
            ]
        
        firstRow = points[0]
        otherRows = points[1:]
        # print(f'row={firstRow}')
        bestSoFar = firstRow   # no penalties for row #0
        # print(f'  {bestSoFar=}')
        print(f'  bestSoFar={bestSoFar[:5]}...{bestSoFar[-5:]}')
        for row in otherRows:
            # print(f'{row=}')
            print(f'  row={row[:5]}...{row[-5:]}')
            prior_row_pairs = [
                (value, oldC)
                for oldC, value in enumerate(bestSoFar)
            ]
            prior_row_pairs.sort(reverse=True)
            newBest = [0] * grid_W
            minBest = 0
            for (value, oldC) in prior_row_pairs:
                if value <= minBest:
                    print(f'  Since {minBest=}, {value=} and later are irrelevant')
                    break
                # print(f'  {oldC=} {value=}')
                
                applyThis = [
                    value + P
                    for P in penalties(oldC)
                ]
                newBest = list(map(max, zip(newBest, applyThis)))
                # print(f'    {newBest=}')
                minBest = min(newBest)

            bestSoFar = list(map(sum, zip(row, newBest)))
            # print(f'  {bestSoFar=}')
            print(f'  bestSoFar={bestSoFar[:5]}...{bestSoFar[-5:]}')

        return max(bestSoFar)
# NOTE: Time Limit Exceeded for large inputs
