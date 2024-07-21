class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:

        endpoints = sorted(set([
            point
            for (start, end, color) in segments
            for point in (start, end)
        ]))
        # print(f'{endpoints=}')
        pairs = tuple(zip(endpoints, endpoints[1:]))
        # print(f'{pairs=}')
        colors = {
            pair: 0
            for pair in pairs
        }
        # print(f'(before) {colors=}')

        pairs_consume = list(pairs)
        for (start, end, color) in sorted(segments):
            # print(f'{(start,end,color)=}')
            pairs_colorized = 0
            for i, pair in enumerate(pairs_consume):
                (A, B) = pair
                if A <= B <= start <= end:
                    # print(f'  {pair=} Delete')
                    pairs_consume[i] = None
                    continue
                if start <= A <= B <= end:
                    # print(f'  {pair=} +{color=}')
                    pairs_colorized += 1
                    colors[pair] += color
                    continue
                if start <= end <= A <= B:
                    # print(f'  {pair=} Quit')
                    break
                raise Exception(f'Should not get here: {(start,end)=}; {pair=}')
            # print(f'  {pairs_colorized} pairs +{color=}')
            while None in pairs_consume:
                pairs_consume.remove(None)
        # print(f'(after) {colors=}')

        answer = [
            (*pair, colorSum)
            for pair, colorSum in colors.items()
            if colorSum
        ]
        return answer
# NOTE: TLE for large inputs.
# NOTE: we should be able to turn the pairs/segments section inside-out
#   so that we can get rid of the Colors dict entirely,
#   and instead create each tuple of the answer left-to-right
