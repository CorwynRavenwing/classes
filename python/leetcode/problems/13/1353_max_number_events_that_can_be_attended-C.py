class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        schedule = []
        # new process:
        # turn each event into a corresponding event-day list
        # e.g. [1 5] -> [1 2 3 4 5]
        event_days = [
            [
                D
                for D in range(eStart, eEnd + 1)
            ]
            for (eStart, eEnd) in events
        ]
        # print(f'{event_days=}')
        all_days = tuple(set([
            D
            for days in event_days
            for D in days
        ]))
        # print(f'{all_days=}')
        # then for each possible day
        for D in all_days:
            # print(f'{schedule=}')
            print(f'{D=}')
            any_events_available_ever = any([
                len(E) > 0
                for E in event_days
            ])
            # print(f'{any_events_available_ever=}')
            if not any_events_available_ever:
                print(f'  No other events available')
                break
            available_events = [
                (
                    max(E) - min(E),    # max(), min() are legal because ...
                    index,
                )
                for index, E in enumerate(event_days)
                if D in E               # ... "if D in E" prevents empty E
            ]
            if not available_events:
                # if no events are available on this day, don't insert anything
                # # or maybe a None
                # print(f'  No available events')
                # schedule.append(None)
                continue
            else:
                print(f'  {available_events=}')
            # select the event, available on that day,
            # that has the shortest number of future available days
            available_events.sort()     # sort by "number of days" field ASC
            (number_of_days, event_index) = available_events[0]
            # add that event to the daily schedule
            print(f'    Selected #{event_index} ({number_of_days} days)')
            schedule.append(event_index)
            # delete the entire event from the event-day list
            # (actually overwrite with [] so we don't lose the index)
            event_days[event_index] = []
            # and delete that day from every event-day list
            event_days = [
                [
                    day
                    for day in E
                    if day != D
                ]
                for E in event_days
            ]
            # event_days_display = [
            #     (
            #         E
            #         if (len(E) == 0)
            #         else
            #         f'[{E[0]}]'
            #         if (len(E) == 1)
            #         else
            #         f'[{E[0]} .. {E[-1]}]'
            #         if (len(E) > 1)
            #         else
            #         '???'
            #     )
            #     for E in event_days
            # ]
            # print(f'-> {event_days_display=}')
        # when done, return a count of the schedule that are not None
        print(f'{schedule=}')
        # while None in schedule:
        #     schedule.remove(None)
        return len(schedule)

# NOTE: gets a Time Limit Exceeded for large inputs
