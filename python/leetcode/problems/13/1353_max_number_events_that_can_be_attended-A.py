class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        schedules = {()}
        for i, event_days in enumerate(events):
            print(f'Event {i}: {event_days=}')
            new_schedules = set()
            (eStart, eEnd) = event_days
            for D in range(eStart, eEnd + 1):
                print(f'  Day {D}')
                for S in schedules:
                    # print(f'    Try {D} in {S}')
                    if D not in S:
                        attendD = tuple(sorted(S + (D,)))
                        # print(f'      -> {attendD}')
                        new_schedules.add(attendD)
            schedules |= new_schedules
        event_counts = [
            len(S)
            for S in schedules
        ]
        print(f'{event_counts=}')
        return max(event_counts)
# NOTE: Memory Limit Exceeded for large inputs
