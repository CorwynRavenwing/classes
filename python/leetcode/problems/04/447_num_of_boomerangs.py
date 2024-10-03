class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        # points must be hashable
        points = tuple(map(tuple, points))

        # SHORTCUT: distance == Sqrt( (x-difference)^2 + (y-difference)^2 )
        # but "equal distances" === "equal *squares of* distances" and
        # we won't need to deal with floating-point rounding errors
        # (and also won't have to absolute-value everything)

        Square = lambda x: (x * x)
        def distanceSquared(point1: Tuple[int,int], point2: Tuple[int,int]) -> int:
            (x1, y1) = point1
            (x2, y2) = point2
            return Square(x1 - x2) + Square(y1 - y2)
        
        pointDistance = {}
        # pointDistance[point][distance] === {p1, p2, p3 ...}
        for P1 in points:
            pointDistance.setdefault(P1, {})
        for i, P1 in enumerate(points):
            for j, P2 in enumerate(points):
                if j <= i:
                    continue
                dist = distanceSquared(P1, P2)
                pointDistance[P1].setdefault(dist, set())
                pointDistance[P2].setdefault(dist, set())
                pointDistance[P1][dist].add(P2)
                pointDistance[P2][dist].add(P1)
        # print(f'{pointDistance=}')

        answer = 0
        for sourcePoint, distanceDict in pointDistance.items():
            # print(f'{sourcePoint}:')
            for distance, otherPoints in distanceDict.items():
                # print(f'  {distance=}')
                count = len(otherPoints)
                if count <= 1:
                    # print(f'    ({count} <= 1)')
                    continue
                print(f'{sourcePoint}:')
                print(f'  {distance=}')
                print(f'    {tuple(otherPoints)[:5]}{"..." if (count > 5) else ""}')
                answer += count * (count - 1)
                # Triangle(), but without dividing by 2,
                # because ABC and CBA are counted separately

        return answer

# NOTE: Accepted on second Run (first was "unhashable type")
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 1073 ms Beats 5.10%
# NOTE: Memory 85.24 MB Beats 5.31%
