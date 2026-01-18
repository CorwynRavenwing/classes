class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        # we borrow some code from #223:

        def rectangleOverlap(coordsA: List[List[int]], coordsB: List[List[int]]) -> Tuple[int,int]:
            # input: coordsA and coordsB are each a tuple of two points: [[x1,y1],[x2,y2]]
            # signifying the bottom-left and top-right corners of a rectangle.
            # output: a tuple of two ints: the length and width of their intersection,
            # or [0,0] if they don't intersect.

            (ax1,ay1), (ax2,ay2) = coordsA
            (bx1,by1), (bx2,by2) = coordsB

            # print(f'A: ({ax1},{ay1}), ({ax2},{ay2})')
            # aX = ax2 - ax1
            # aY = ay2 - ay1
            # aArea = aX * aY
            # print(f'A Size: {aX} x {aY}: {aArea}')

            # print(f'B: ({bx1},{by1}), ({bx2},{by2})')
            # bX = bx2 - bx1
            # bY = by2 - by1
            # bArea = bX * bY
            # print(f'B Size: {bX} x {bY}: {bArea}')

            cx1 = max(ax1, bx1)
            cy1 = max(ay1, by1)

            cx2 = min(ax2, bx2)
            cy2 = min(ay2, by2)

            # print(f'C: ({cx1},{cy1}), ({cx2},{cy2})')
            cX = cx2 - cx1
            cY = cy2 - cy1
            cArea = cX * cY if (cX > 0) and (cY > 0) else 0
            # print(f'C Size: {cX} x {cY}: {cArea}')
            return (cX, cY) if cArea else (0,0)
        
        maxSize = 0
        rectangles = tuple(zip(bottomLeft, topRight))
        for i, A in enumerate(rectangles):
            # print(f'{i=} {A=}')
            for j, B in enumerate(rectangles):
                if j <= i:
                    continue
                # print(f'  {j=} {B=}')
                overlap = rectangleOverlap(A, B)
                # if overlap != (0,0):
                #     print(f'    {overlap=}')
                maxSize = max(
                    maxSize,
                    min(overlap)
                    # side length of a square that will fit in this rectangle
                )
                # print(f'    {maxSize=}')
        
        return maxSize * maxSize    # are of this square

# NOTE: Runtime 6941 ms Beats 13.90%
# NOTE: Memory 17.53 MB Beats 5.88%
