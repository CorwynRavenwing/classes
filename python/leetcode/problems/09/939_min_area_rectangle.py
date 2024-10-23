class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        pointsX = {}
        pointsY = {}
        for P in points:
            (X, Y) = P
            pointsX.setdefault(X, set())
            pointsY.setdefault(Y, set())
            pointsX[X].add(Y)
            pointsY[Y].add(X)
        
        print(f'{pointsX=}')
        print(f'{pointsY=}')

        answers = []
        for X1, X1set in pointsX.items():
            for X2, X2set in pointsX.items():
                # WLOG we make X1 < X2
                if X1 >= X2:
                    continue
                intersect = X1set & X2set
                if not intersect:
                    continue
                if len(intersect) < 2:
                    continue
                for Y1, Y2 in pairwise(sorted(intersect)):
                    # pairwise sorted because we're looking for minimum area
                    # and therefore we want Y1,Y2 to be close together
                    area = (X2 - X1) * (Y2 - Y1)
                    print(f'{area}: ({X1},{Y1}),({X2},{Y2})')
                    # will both be positive because of ordering
                    answers.append(area)

        print(f'{answers=}')
        return min(answers, default=0)

# NOTE: Accepted on second Run (first was variable-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 540 ms Beats 83.97%
# NOTE: O(N^2)
# NOTE: Memory 19.04 MB Beats 6.10%
# NOTE: O(N)
