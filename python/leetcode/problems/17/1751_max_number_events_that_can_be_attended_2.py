class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        events.sort()

        def DP_skip(index: int, k: int) -> int:
            return DP(index + 1, k)

        def DP_pick(index: int, k: int) -> int:
            (startTime, endTime, value) = events[index]
            next_possible_event = [endTime + 1, 0, 0]
            new_index = bisect_left(
                events,
                next_possible_event,
                index + 1
            )
            new_k = k - 1
            return value + DP(new_index, new_k)

        @cache
        def DP(index: int, k: int) -> int:
            print(f'DP({index},{k})')
            if k == 0:
                return 0
            try:
                check = events[index]
            except IndexError:
                return 0
            return max([
                DP_skip(index, k),
                DP_pick(index, k),
            ])

        return DP(0, k)

# NOTE: Acceptance Rate 61.0% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded: cache)
# NOTE: Runtime 2213 ms Beats 13.18%
# NOTE: Memory 261.51 MB Beats 26.37%
