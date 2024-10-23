class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        Square = lambda x: x * x

        # SHORTCUT: "smallest distance" === "smallest distance squared"

        def DistSquared(P1: Tuple[int,int], P2: Tuple[int,int]) -> int:
            (X1, Y1) = P1
            (X2, Y2) = P2
            return Square(X1-X2) + Square(Y1-Y2)
        
        points.sort(
            key=lambda Point: DistSquared(Point, (0,0))
        )
        return points[:k]

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 50 ms Beats 98.97%
# NOTE: Memory 21.01 MB Beats 99.12%
