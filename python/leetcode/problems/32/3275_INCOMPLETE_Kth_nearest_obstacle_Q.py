class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:

        obstacles = []
        prior_distance = float('+inf')

        def doQuery(Q: List[int]) -> int:
            nonlocal prior_distance
            nonlocal obstacles
            # print(f'{Q=}')
            (X, Y) = Q
            distance_from_origin = abs(X) + abs(Y)
            if distance_from_origin >= prior_distance:
                print(f'  Not saving {distance_from_origin}: > {prior_distance}')
            else:
                bisect.insort(obstacles, distance_from_origin)
                # print(f'  {obstacles=}')
                if len(obstacles) > k:
                    obstacles = obstacles[:k]   # anything farther away: throw out

            try:
                distance_to_kth_obstacle = obstacles[k - 1]
            except IndexError:
                # print(f'  {None}: no such obstacle')
                return -1

            # print(f'  {distance_to_kth_obstacle=}')
            prior_distance = distance_to_kth_obstacle
            return distance_to_kth_obstacle

        # if k == 75000:
        #     print(f'This one. {len(queries)=}')
        #     return [-1]

        if len(queries) < k:
            return [-1] * len(queries)

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Timeout for huge inputs
# NOTE: Acceptance Rate 47.4%
