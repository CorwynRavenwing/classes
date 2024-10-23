class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        
        # A hint from the comments: two line segments make a rectangle
        # (UL-LR and UR-LL) if and only if they share the same length
        # and midpoint.

        # SHORTCUT: length is SQRT[ (X2-X1)^2 + (Y2-Y1)^2 ], but to
        # avoid floating-point (and because we only care if things
        # are equal) we will avoid taking SQRT[].

        # SHORTCUT: midpoint is ( (X1+X2)/2, (Y1+Y2)/2 ), but again,
        # to avoid floating-point and because we only care about
        # equality, we will avoid dividing both numbers by 2.

        # points must be hashable.
        points = tuple(map(tuple, points))

        # store pairs of points, grouped by the above rules
        pointPairs = {}

        Square = lambda x: x * x
        Sqrt = lambda x: x ** 0.5

        for i, P1 in enumerate(points):
            for j, P2 in enumerate(points):
                if i >= j:
                    continue
                # print(f'{i}:{P1}, {j}:{P2}')
                (X1, Y1) = P1
                (X2, Y2) = P2

                midpoint_doubled = (X1+X2, Y1+Y2)
                length_squared = Square(X2 - X1) + Square(Y2 - Y1)
                rule = (length_squared, midpoint_doubled)
                pair = (P1, P2)
                # print(f'  {rule=}')
                
                pointPairs.setdefault(rule, set())
                pointPairs[rule].add(pair)
        
        print(f'pointPairs:')
        for rule, pointGroups in pointPairs.items():
            print(f'  R={rule}:')
            for pair in pointGroups:
                print(f'    P={pair}')
        
        answers = []
        # sort by length: smallest diagonal === smallest area (?)
        for rule, pointGroups in sorted(pointPairs.items()):
            print(f'  R={rule}:')
            if len(pointGroups) == 1:
                # only 1 line segment here
                continue
            for i, pair1 in enumerate(pointGroups):
                for j, pair2 in enumerate(pointGroups):
                    if i >= j:
                        continue
                    (P1, P2) = pair1    # the hypotenuse
                    (P3, P4) = pair2    # pick either one as the corner

                    (X1, Y1) = P1
                    (X2, Y2) = P2
                    (X3, Y3) = P3
                    # ignore point 4
                    height = Sqrt(Square(X1 - X3) + Square(Y1 - Y3))
                    width = Sqrt(Square(X2 - X3) + Square(Y2 - Y3))
                    area = height * width
                    print(f'A={area} = H={height} * W={width}')
                    answers.append(area)

        print(f'{answers=}')
        return min(answers, default=0)

# NOTE: Accepted on first Submit
# NOTE: Runtime 184 ms Beats 28.13%
# NOTE: Memory 17.81 MB Beats 8.20%
