class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        
        # we borrow some code from #3623:
        def Nchoose2(N: int) -> int:
            return N * (N - 1) // 2

        # Euclidian Algorithm for GCD, as described in Wikipedia
        def GCD(A: int, B: int) -> int:
            # print(f'GCD({A},{B})')
            if B == 0:
                return A
            else:
                return GCD(B, A % B)
        
        def slope(P1: List[int], P2: List[int]) -> List[int]:
            (x1, y1) = P1
            (x2, y2) = P2
            dx = x2 - x1
            dy = y2 - y1
            if dy < 0:
                dx *= -1
                dy *= -1
            divisor = GCD(dx, dy)
            dx //= divisor
            dy //= divisor
            answer = (dx, dy)
            print(f'slope({P1};{P2}) / {divisor} == {answer}')
            return answer
        
        for (P1, P2) in combinations(points, 2):
            S = slope(P1, P2)
            # then bucket the line-segments by their slope
        
        # for each Slope bucket
        # there are Nchoose2(len(bucket)) possibe pairs of line-segments
        # except parallelograms are counted twice
        # == pairs of line segments that share a midpoint
        # == share [(x1+x2)/2,(y1+y)/2]
        # == share [x1+x2,y1+y2] to avoid division
        # ALSO never count zero-area figures
        # == slope between one point of each segment is also Slope

'''
    def countTrapezoids(self, points: List[List[int]]) -> int:

        mod = 10 ** 9 + 7

        Xs_by_Y = Counter()
        for (x, y) in points:
            Xs_by_Y[y] += 1
        # print(f'{Xs_by_Y=}')

        X_values_by_Y = [
            Nchoose2(x_count)
            for x_count in Xs_by_Y.values()
            if x_count >= 2
        ]
        # print(f'{X_values_by_Y=}')

        answer = 0
        # print(f'(begin) {answer=}')
        for (a, b) in combinations(X_values_by_Y, 2):
            answer += (a * b)
            answer %= mod
            # print(f'({a},{b}) {answer=}')

        return answer % mod
'''

# NOTE: Acceptance Rate 40.5% (HARD)

# NOTE: A complex algorithm and no time to make it happen
