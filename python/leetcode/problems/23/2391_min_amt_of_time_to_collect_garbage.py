class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        def stuffCollectionTime(stuffType: str) -> int:
            nonlocal garbage
            nonlocal travel
            filtered = [
                ''.join([
                    stuff
                    for stuff in house
                    if stuff == stuffType
                ])
                for house in garbage
            ]
            # print(f'{stuffType}: {filtered}')
            while filtered and filtered[-1] == '':
                _ = filtered.pop(-1)
            print(f'{stuffType}: {filtered}')
            pickupTimes = tuple(map(len, filtered))
            houses = len(filtered)
            travelTimes = travel[:houses - 1] if houses else []
            print(f'{pickupTimes=}')
            print(f'{travelTimes=}')
            return sum(pickupTimes) + sum(travelTimes)
        
        return sum([
            stuffCollectionTime('G'),
            stuffCollectionTime('P'),
            stuffCollectionTime('M'),
        ])

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 475 ms Beats 5.25%
# NOTE: Memory 38.79 MB Beats 29.28%
