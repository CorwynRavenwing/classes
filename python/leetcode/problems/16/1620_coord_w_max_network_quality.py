class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:

        radiusSquared = radius * radius

        distanceCache = {}
        def PythagorasXY(xDist: int, yDist: int) -> int:
            coord = (abs(xDist), abs(yDist))
            if coord not in distanceCache:
                distanceCache[coord] = (xDist * xDist) + (yDist * yDist)
            #     print(f'Pxy({coord}) = {distanceCache[coord]}')
            # else:
            #     print(f'Pxy({coord}) = cache hit')
            return distanceCache[coord]

        def Pythagoras(coord1: Tuple[int,int], coord2: Tuple[int,int]) -> int:
            (X1, Y1) = coord1
            (X2, Y2) = coord2
            return PythagorasXY(X1 - X2, Y1 - Y2)
        
        qualityCache = {}
        def quality(Qi: int, distanceSquared: int) -> int:
            query = (Qi, distanceSquared)
            if query not in qualityCache:
                distance = sqrt(distanceSquared)
                qualityCache[query] = int(Qi // (1 + distance))
            #     print(f'Q({query}) = {qualityCache[query]}')
            # else:
            #     print(f'Q({query}) = CACHE HIT')
            return qualityCache[query]

        strength_at_point = Counter()    # e.g. { (X, Y): sum(Q) }
        origin = (0, 0)
        strength_at_point[origin] = 0   # so it appears in the qualities list

        for (Xi, Yi, Qi) in towers:
            towerPos = (Xi, Yi)
            print(f'Tower {towerPos} Q={Qi}')
            for X in range(Xi - radius, Xi + radius + 1):
                for Y in range(Yi - radius, Yi + radius + 1):
                    coord = (X, Y)
                    distanceSquared = Pythagoras(towerPos, coord)
                    if distanceSquared > radiusSquared:
                        continue
                    strength_at_point[coord] += quality(Qi, distanceSquared)
        # print(f'{strength_at_point=}')
        max_strength = max(strength_at_point.values())
        print(f'{max_strength=}')
        points_at_max = [
            coord
            for coord, strength in strength_at_point.items()
            if strength == max_strength
        ]
        print(f'{points_at_max=}')
        if len(points_at_max) == 1:
            return points_at_max[0]
        
        points_with_nonnegative_coords = [
            (x, y)
            for (x, y) in points_at_max
            if (x >= 0) and (y >= 0)
        ]
        return min(points_with_nonnegative_coords)

