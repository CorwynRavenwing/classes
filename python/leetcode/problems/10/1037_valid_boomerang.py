class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
        def distinct(points: List[List[int]]) -> bool:
            (A, B, C) = points
            # print(f"{A=} {B=} {C=}")
            # print(f"  {(A != B)} {(B != C)} {(A != C)}")
            return (A != B) and (B != C) and (A != C)
        
        def straightLine(points: List[List[int]]) -> bool:
            (A, B, C) = points
            (Ax, Ay) = A
            (Bx, By) = B
            (Cx, Cy) = C
            AB = (Bx - Ax) / (By - Ay) if (By - Ay) else None
            AC = (Cx - Ax) / (Cy - Ay) if (Cy - Ay) else None
            print(f"{A=} {B=} {C=}")
            print(f"  {AB=} {AC=}")
            return (AB == AC)
        
        return (
            (
                len(points) == 3
            ) and (
                distinct(points)
            ) and not (
                straightLine(points)
            )
        )

