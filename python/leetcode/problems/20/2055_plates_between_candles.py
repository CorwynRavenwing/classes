class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        plates = [
            (
                1
                if ch == '*'
                else 0
            )
            for ch in s
        ]
        candleIndexes = [
            index
            for index, ch in enumerate(s)
            if ch == '|'
        ]
        candles = [
            (
                1
                if ch == '|'
                else 0
            )
            for ch in s
        ]
        assert sum(plates) + sum(candles) == len(s)
        # print(f' {plates=}')
        # print(f'{candles=}')
        plateSums = list(itertools.accumulate(plates))
        # print(f'{plateSums=}')
        print(f'{candleIndexes=}')

        def doQuery(query: Tuple[int,int]) -> int:
            # print(f'{query=}')
            (leftI, rightI) = query
            leftCandleIndex = bisect_left(candleIndexes, leftI)
            if leftCandleIndex >= len(candleIndexes):
                print(f'{leftCandleIndex=} >= {len(candleIndexes)=}, out of range!')
                return 0
            rightCandleIndex = bisect_right(candleIndexes, rightI)
            if rightCandleIndex >= len(candleIndexes):
                # print(f'  (right index {rightCandleIndex} -=1: past end)')
                rightCandleIndex -= 1
                if rightCandleIndex < 0:
                    # print(f'    (but {rightCandleIndex} is too low)')
                    return 0
            if candleIndexes[rightCandleIndex] > rightI:
                # print(f'  (right index -=1: {candleIndexes[rightCandleIndex]} too high)')
                rightCandleIndex -= 1
                if rightCandleIndex < 0:
                    # print(f'    (but {rightCandleIndex} is too low)')
                    return 0
            # print(f'{leftCandleIndex=} {rightCandleIndex=}')

            leftCandle = candleIndexes[leftCandleIndex]
            rightCandle = candleIndexes[rightCandleIndex]
            # print(f'  {leftCandle=} {rightCandle=}')
            if leftCandle > rightCandle:
                return 0

            # we dont have to use leftCandle-1 b/c the sum will not have changed,
            # since this is a *candle* and the sum only rises at *plates*
            leftPlate = plateSums[leftCandle]
            rightPlate = plateSums[rightCandle]
            # print(f'  {leftPlate=} {rightPlate=}')

            return rightPlate - leftPlate
        
        return [
            doQuery(Q)
            for Q in queries
        ]
# NOTE: Runtime 1551 ms Beats 31.09%
# NOTE: Memory 55.76 MB Beats 57.21%
