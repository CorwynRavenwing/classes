class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        Square = lambda x: x * x

        def pointIsInCircle(point: List[int], center_x, center_y, radius) -> bool:
            # print(f'  PiC({point},({center_x},{center_y})+{radius})')
            (X, Y) = point
            # check bounding box first:
            if not (center_x - radius <= X <= center_x + radius): return False
            if not (center_y - radius <= Y <= center_y + radius): return False
            # now check circle itself:
            distanceSquared = sum([
                Square(center_x - X),
                Square(center_y - Y),
            ])
            radiusSquared = Square(radius)
            # compare squares b/c (1) roots are expensive and (2) avoid float errors
            return distanceSquared <= radiusSquared
        
        def doQuery(Q: List[int]) -> int:
            print(f'{Q=}')
            (center_x, center_y, radius) = Q
            points_inside_circle = [
                (
                    1
                    if pointIsInCircle(point, center_x, center_y, radius)
                    else
                    0
                )
                for point in points
            ]
            return sum(points_inside_circle)

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 789 ms Beats 6.77%
# NOTE: Memory 17.76 MB Beats 6.52%
