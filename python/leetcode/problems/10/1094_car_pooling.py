class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        stops = []
        for (count, fromI, toI) in trips:
            if count > capacity:
                print(f'NO: cannot move {count} people')
                return False
            if fromI > toI:
                print(f'NO: cannot drive westward')
                return False
            stops.append((fromI, +count))
            stops.append((toI, -count))
        stops.sort()    # default sort: location first; negative count earlier
        # print(f'{stops=}')
        
        passengers = 0
        for (location, count) in stops:
            passengers += count
            print(f'{location}: {count:+d} ({passengers})')
            if passengers > capacity:
                print(f'  NO: overflow')
                return False

        return True

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 4 ms Beats 35.87%
# NOTE: Memory 17.16 MB Beats 31.96%
