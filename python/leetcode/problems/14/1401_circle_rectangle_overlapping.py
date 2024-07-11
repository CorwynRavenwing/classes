class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        xSection = (
            'A'
            if (x1 <= xCenter <= x2)
            else 'B'
            if (x1 - radius <= xCenter <= x2 + radius)
            else 'C'
        )
        ySection = (
            'A'
            if (y1 <= yCenter <= y2)
            else 'B'
            if (y1 - radius <= yCenter <= y2 + radius)
            else 'C'
        )
        location = ''.join(sorted([xSection,ySection]))
            
        if (location == 'AA'):
            print(f'YES: center of circle is within rectangle')
            return True
        if ('C' in location):   # AC CA BC CB CC
            print(f'NO: too far away to intersect, X={xSection} Y={ySection}')
            return False
        if (location == 'AB'):  # AB BA
            print(f'YES: overlap like Example 1')
            return True
        if (location == 'BB'):
            print(f'Unsure: checking distances')
            square = lambda x: x * x
            xDistSqr = min([
                square(xCenter - X)
                for X in [x1, x2]
            ])
            yDistSqr = min([
                square(yCenter - Y)
                for Y in [y1, y2]
            ])
            rSqr = square(radius)
            distanceSqr = xDistSqr + yDistSqr
            if distanceSqr <= rSqr:
                print(f'YES: {distanceSqr} <= {rSqr}')
                return True
            else:
                print(f'NO: {distanceSqr} > {rSqr}')
                return False
# NOTE: 27 ms; Beats 95.04%
