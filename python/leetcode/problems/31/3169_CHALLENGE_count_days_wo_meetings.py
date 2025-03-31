class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        meetings.append([0,0])              # fictional begin-of-time meeting
        meetings.append([days + 1,None])    # fictional end-of-time meeting
        # print(f'{meetings=}')
        meetings.sort()
        # print(f'{meetings=}')
        meetings = list(map(tuple, meetings))
        # print(f'{meetings=}')
        for i in range(1, len(meetings)):
            prev_start, prev_end = meetings[i - 1]
            this_start, this_end = meetings[i]
            if prev_start == this_start:
                # meetings share start time: merge, use latest end time
                meetings[i - 1] = None
                meetings[i] = (prev_start, max(prev_end, this_end))
            elif prev_end >= this_start:
                # meetings overlap: merge, use earliest begin time and latest end time
                meetings[i - 1] = None
                meetings[i] = (prev_start, max(prev_end, this_end))
        print(f'{len(meetings)=}')
        while None in meetings:
            meetings.remove(None)
        print(f'{len(meetings)=}')
        print(f'{meetings=}')

        answers = [
            this_start - prev_end - 1
            for (
                (prev_start, prev_end),
                (this_start, this_end)
            ) in pairwise(meetings)
        ]
        print(f'{answers=}')

        return sum(answers)

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

# NOTE: Accepted on first Submit
# NOTE: Runtime 3448 ms Beats 5.12%
# NOTE: Memory 66.88 MB Beats 45.54%

# NOTE: re-ran for challenge:
# NOTE: Runtime 2234 ms Beats 5.04%
# NOTE: Memory 53.58 MB Beats 13.60%
