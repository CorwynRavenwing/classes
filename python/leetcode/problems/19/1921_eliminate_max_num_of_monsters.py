class Solution:
    def eliminateMaximum(self, distance_list: List[int], speed_list: List[int]) -> int:
        
        times_to_arrival = [
            distance / speed
            for distance, speed in zip(distance_list, speed_list)
        ]
        times_to_arrival.sort()
        print(f'{times_to_arrival=}')

        answer = 0
        for second, time in enumerate(times_to_arrival):
            if second < time:
                print(f'{second}: {time} ok')
                answer += 1
            else:
                print(f'{second}: {time} LOSE')
                break
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 267 ms Beats 5.18%
# NOTE: Memory 32.60 MB Beats 23.30%
