class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        print(f'A: ({ax1},{ay1}), ({ax2},{ay2})')
        aX = ax2 - ax1
        aY = ay2 - ay1
        aArea = aX * aY
        print(f'A Size: {aX} x {aY}: {aArea}')

        print(f'B: ({bx1},{by1}), ({bx2},{by2})')
        bX = bx2 - bx1
        bY = by2 - by1
        bArea = bX * bY
        print(f'B Size: {bX} x {bY}: {bArea}')

        cx1 = max(ax1, bx1)
        cy1 = max(ay1, by1)

        cx2 = min(ax2, bx2)
        cy2 = min(ay2, by2)

        print(f'C: ({cx1},{cy1}), ({cx2},{cy2})')
        cX = cx2 - cx1
        cY = cy2 - cy1
        cArea = cX * cY if (cX > 0) and (cY > 0) else 0
        print(f'C Size: {cX} x {cY}: {cArea}')
        return aArea + bArea - cArea

