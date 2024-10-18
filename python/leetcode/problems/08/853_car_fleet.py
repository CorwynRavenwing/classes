class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        distances_and_speeds = [
            (
                (target - posI),
                speedI,
            )
            for (posI, speedI) in zip(position, speed)
        ]
        # print(f'{distances_and_speeds=}')

        distances_and_times = [
            (
                distanceI,
                distanceI / speedI,
            )
            for (distanceI, speedI) in distances_and_speeds
        ]
        # print(f'raw {distances_and_times=}')
        distances_and_times.sort()
        # print(f'sorted {distances_and_times=}')

        for i in range(1, len(distances_and_times)):
            (prev_dist, prev_time) = distances_and_times[i - 1]
            (this_dist, this_time) = distances_and_times[i]
            if prev_time >= this_time:
                print(f'Merge {i=}')
                distances_and_times[i - 1] = None
                distances_and_times[i] = (this_dist, prev_time)
        while None in distances_and_times:
            distances_and_times.remove(None)
        print(f'{distances_and_times=}')
        
        return len(distances_and_times)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 1888 ms Beats 5.03%
# NOTE: Memory 49.36 MB Beats 5.03%
