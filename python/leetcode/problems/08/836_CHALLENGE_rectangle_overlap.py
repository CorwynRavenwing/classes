class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

        (r1x1, r1y1, r1x2, r1y2) = rec1
        (r2x1, r2y1, r2x2, r2y2) = rec2

        print(f"{rec1=}")
        print(f"{rec2=}")

        x1 = max(r1x1, r2x1)
        y1 = max(r1y1, r2y1)

        x2 = min(r1x2, r2x2)
        y2 = min(r1y2, r2y2)

        print(f"overlap: ({x1},{y1}) ({x2},{y2})")
        xSpan = x2 - x1
        ySpan = y2 - y1
        print(f"span: ({xSpan}, {ySpan})")
        xSpan = max(0, xSpan)
        ySpan = max(0, ySpan)
        print(f"trunc:({xSpan}, {ySpan})")
        size = xSpan * ySpan
        print(f"size: {size}")

        return (size > 0)

# NOTE: Acceptance Rate 47.1% (easy)

# NOTE: re-ran for challenge:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.27 MB Beats 59.18%
