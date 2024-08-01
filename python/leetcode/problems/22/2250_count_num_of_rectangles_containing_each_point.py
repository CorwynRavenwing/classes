class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:

        rectanglesByHeight = {}
        for (Li, Hi) in rectangles:
            rectanglesByHeight.setdefault(Hi, [])
            bisect.insort(rectanglesByHeight[Hi], Li)
        # print(f'{rectanglesByHeight=}')
        available_heights = sorted(
            rectanglesByHeight.keys()
        )
        # print(f'{available_heights=}')

        def CountRectanglesForPoint(P: List[int]) -> int:
            # print(f'CRFP({P}):')
            (X, Y) = P
            first_Y_index = bisect_left(available_heights, Y)
            # print(f'  {first_Y_index=}')
            heights = available_heights[first_Y_index:]
            # print(f'  {len(heights)=}')
            answer = 0
            for H in heights:
                # print(f'    {H=}')
                if Y > H:
                    print(f'    oops, too high')
                    continue
                available_lengths = rectanglesByHeight[H]
                first_X_index = bisect_left(available_lengths, X)
                # print(f'      {first_X_index=}')
                lengths = available_lengths[first_X_index:]
                # print(f'      +{len(lengths)}')
                answer += len(lengths)

            return answer

        return [
            CountRectanglesForPoint(P)
            for P in points
        ]

