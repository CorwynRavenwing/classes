class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        events.sort(
            key=lambda x: (x[1] - x[0], x[0], x[1])
        )
        print(f'sorted: {events=}')

        schedule = ()
        for i, event_days in enumerate(events):
            print(f'Event {i}: {event_days=}')
            (eStart, eEnd) = event_days
            for D in range(eStart, eEnd + 1):
                print(f'  Day {D}')
                if D not in schedule:
                    schedule = schedule + (D,)
                    print(f'      -> {schedule}')
                    break
        event_count = len(schedule)
        return event_count

# NOTE: starts getting wrong answers for data sets with
# short time periods that sort later than long time periods
