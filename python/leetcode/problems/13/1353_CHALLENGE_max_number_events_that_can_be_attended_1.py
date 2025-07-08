class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        # default sort will give us the order we need:
        # first by start_day ASC then by end_day ASC
        events.sort()

        available = []
        start_day_set = set()
        events_dict = {}
        for (start_day, end_day) in events:
            start_day_set.add(start_day)
            events_dict.setdefault(start_day, [])
            events_dict[start_day].append(end_day)
        start_days = list(sorted(start_day_set))
        
        # print(f'{start_day_set=}')
        # print(f'{start_days=}')
        # print(f'{events_dict=}')

        day = 0
        answer = 0
        while available or start_days:
            if not available:
                while start_days and start_days[0] < day:
                    skip_day = start_days.pop(0)
                    # print(f'SKIP {skip_day} < {day}')
                if not start_days:
                    # print(f'Out of data {available=} {start_days=}')
                    continue
                day = start_days[0]
                # print(f'Jump to {day=}')
            # whether available exists or not:
            if start_days:
                next_day = start_days[0]
                if next_day <= day:
                    # print(f'Grab {next_day} <= {day}:')
                    end_days = events_dict[day]
                    # print(f'  -> {end_days=}')
                    for E in end_days:
                        bisect.insort(available, E)
                    # print(f'  -> {available=}')
                    _ = start_days.pop(0)
                # else:
                #     # print(f'NO {next_day} > {day}')
            # else:
            #     # print(f'NO {start_days=}')
            while available and available[0] < day:
                skip_event = available.pop(0)
                # print(f'SKIP {skip_event} < {day}')
            if available:
                take_event = available.pop(0)
                # print(f'{day=}: {take_event=}')
                answer += 1
                day += 1

        return answer

# NOTE: Acceptance Rate 38.4% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 1122 ms Beats 5.03%
# NOTE: Memory 54.14 MB Beats 15.45%

# NOTE: re-ran for challenge:
# NOTE: Runtime 1081 ms Beats 5.03%
# NOTE: Memory 53.76 MB Beats 17.39%
