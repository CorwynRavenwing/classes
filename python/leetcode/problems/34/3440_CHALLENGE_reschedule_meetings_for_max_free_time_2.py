class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        
        # we borrow some code from #3439:

        events = list(
            zip(startTime, endTime)
        )
        event_lengths = [
            B - A
            for A, B in events
        ]
        # print(f'{event_lengths=}')

        events = (
            [
                (None, 0)           # imaginary event ending at time 0
            ] + events + [
                (eventTime, None)   # imaginary event starting at event end
            ]
        )
        # print(f'{events=}')

        gaps = [
            B_start - A_end
            for ((A_start, A_end), (B_start, B_end)) in pairwise(events)
        ]
        # print(f'{gaps=}')

        partialSums = (0,) + tuple(accumulate(gaps))
        # print(f'{partialSums=}')

        k = 1   # for this version, only move 1 meeting:

        partialShifted = partialSums[k + 1:]
        # print(f'{partialShifted=}')

        freeTimes = tuple(
            B - A
            for (A, B) in zip(partialSums, partialShifted)
        )
        # print(f'{freeTimes=}')

        answer_keeping_order = max(freeTimes)

        answer_changing_order = 0
        gaps_available = Counter(gaps)
        # print(f'{gaps_available=}')
        for i, event_size in enumerate(event_lengths):
            # print(f'[{i}]: {event_size}')
            gaps_adjacent = gaps[i:i + 2]   # pick 2, numbers i and i+1
            new_event_size = event_size + sum(gaps_adjacent)
            if answer_changing_order > new_event_size:
                # print(f'  -> would not help: {new_event_size} < max')
                continue
            gaps_not_adjacent_count = gaps_available - Counter(gaps_adjacent)
            gaps_not_adjacent = tuple(gaps_not_adjacent_count.keys())
            # print(f'  {gaps_adjacent=}')
            # print(f'  {gaps_not_adjacent=}')
            # print(f'  {max(gaps_not_adjacent)=}')
            if max(gaps_not_adjacent) >= event_size:
                # print(f'  Move event: answer={event_size} + {gaps_adjacent}')
                answer_changing_order = max(answer_changing_order, new_event_size)
            # else:
            #     # print(f'  Cannot move event: no gap big enough')

        return max(answer_keeping_order, answer_changing_order)

# NOTE: Acceptance Rate 40.9% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on fifth Submit (edge case: moving makes it worse; Output Exceeded; Time Limit Exceeded; Output Exceeded again)
# NOTE: Runtime 552 ms Beats 11.56%
# NOTE: Memory 55.26 MB Beats 5.20%
