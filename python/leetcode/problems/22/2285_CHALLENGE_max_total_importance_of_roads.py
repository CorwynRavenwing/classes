class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:

        # strategy: after assigning numbers to cities, each number appears
        # in the final total once for every road to/from that city.
        # therefore, we place numbers onto cities, largest number onto largest
        # number of roads with that city as an endpoint

        # then, the total score is the sum of (number assigned) * (road count)

        endpoints = [
            city
            for road in roads
            for city in road
        ]
        print(f'{endpoints=}')
        city_counts = Counter(endpoints)
        print(f'{city_counts=}')
        cities_by_count = [
            count   # (count, city)
            for city, count in city_counts.items()
        ]
        while len(cities_by_count) < n:
            cities_by_count.append(0)
        cities_by_count.sort(reverse=True)
        print(f'{cities_by_count=}')
        importances = [
            (n - i) * count
            for i, count in enumerate(cities_by_count)
        ]
        print(f'{importances=}')
        return sum(importances)

