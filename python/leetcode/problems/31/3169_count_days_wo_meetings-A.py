class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        days_endpoints = [0] * (days + 2)
        for (startI, endI) in meetings:
            days_endpoints[startI] += 1
            days_endpoints[endI+1] -= 1
        # print(f'{days_endpoints=}')
        days_meetings = tuple(accumulate(days_endpoints))
        print(f'{days_meetings=}')
        days_nomeeting = [
            index
            for index, day in enumerate(days_meetings)
            if day == 0
        ]
        print(f'{days_nomeeting=}')
        return len(days_nomeeting) - 2
        # the -2 is because the 0th and N+1th indexes will appear in
        # the no-meeting list, but those days don't exist in the range

# NOTE: out of memory error for large input
