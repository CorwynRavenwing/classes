class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        
        # SHORTCUT: to avoid floating-point arithmetic,
        # we record only Distance Squared (X^2 + Y^2)
        # and compare to Radius Squared

        Square = lambda x: (x * x)

        def DistanceSquared(point1: Tuple[int,int], point2: Tuple[int,int]) -> int:
            (X1, Y1) = point1
            (X2, Y2) = point2
            Xdist = Square(X1 - X2)
            Ydist = Square(Y1 - Y2)
            return Xdist + Ydist
        
        def PossiblePoints(point: Tuple[int,int], radius: int) -> List[Tuple[int,int]]:
            (X, Y) = point
            for Xj in range(X - radius, X + radius + 1):
                for Yj in range(Y - radius, Y + radius + 1):
                    yield (Xj, Yj)
            return

        answer = set()
        seen = set()
        for circle in circles:
            circle = tuple(circle)
            if circle in seen:
                # print(f'Circle {circle} seen')
                continue
            else:
                seen.add(circle)
            (Xi, Yi, Ri) = circle
            print(f'Circle [{Xi},{Yi}]+{Ri}')
            radiusSquared = Square(Ri)
            center = (Xi, Yi)
            for point in PossiblePoints(center, Ri):
                if point in answer:
                    # print(f'  {point}: seen')
                    continue
                distSquared = DistanceSquared(center, point)
                if distSquared <= radiusSquared:
                    # print(f'  {point}: yes')
                    answer.add(point)
                    continue
                # else:
                #     print(f'  {point}: no')
        
        # print(f'\n{answer=}')
        return len(answer)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 323 ms Beats 94.22%
# NOTE: Memory 22.27 MB Beats 55.56%
