class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        answer = 0
        first_day = float('+inf')
        last_day = float('-inf')
        for (eStart, eEnd) in events:
            first_day = min(first_day, eStart)
            last_day = max(last_day, eEnd)
        print(f'Day Range: {first_day}..{last_day}')
        # then for each possible day
        while first_day <= last_day:
            D = first_day
            while [] in events:
                events.remove([])
            events.sort(
                key=lambda x: ((x[-1] - min(D, x[0])), x[0])
                # sort by number-of-days ASC (with D as minimum StartDay),
                # then by first-day ASC
            )
            if len(events) > 5:
                print(f'{D=} #E={len(events)}')
                # print(f'{D=} {first_day}..{last_day} #E={len(events)}')
            else:
                print(f'{D=} {first_day}..{last_day} E={events}')
            any_events_available_ever = any([
                len(E) > 0
                for E in events
            ])
            # # print(f'{any_events_available_ever=}')
            if not any_events_available_ever:
                print(f'  No other events available')
                break
            chosen_event = None
            for index, (eStart, eEnd) in enumerate(events):
                if eEnd < D:
                    print(f'  Impossible to attend event #{index}: {eEnd} < {D}')
                    events[index] = []
                    continue
                if eStart <= D <= eEnd:
                    print(f'  Event #{index}')
                    # print(f'  Choose event #{index}: {eStart}..{eEnd}')
                    chosen_event = index
                    break
            if chosen_event is None:
                # if no events are available on this day, skip
                # print(f'  No available events')
                pass
            else:
                # select the event, available on that day,
                # that has the shortest number of future available days
                # add that event to the daily schedule
                answer += 1
                # delete the entire event from the events list
                del events[chosen_event]
                # then delete this day from all events
                while [] in events:
                    events.remove([])
            first_day = float('+inf')
            last_day = float('-inf')
            for (eStart, eEnd) in events:
                # include D + 1 here so days can't go backwards
                first_day = max(D + 1, min(first_day, eStart))
                last_day = max(last_day, eEnd)
            # if D < first_day:
            #     continue
        # when done, return number of scheduled events
        return answer

# NOTE: giving Time Limit Exceeded in pathological cases
