class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:

        events = (
            [
                (None, 0)           # imaginary event ending at time 0
            ] + list(
                zip(startTime, endTime)
            ) + [
                (eventTime, None)   # imaginary event starting at event end
            ]
        )
        print(f'{events=}')

        gaps = [
            B_start - A_end
            for ((A_start, A_end), (B_start, B_end)) in pairwise(events)
        ]
        print(f'{gaps=}')

        partialSums = (0,) + tuple(accumulate(gaps))
        print(f'{partialSums=}')

        partialShifted = partialSums[k + 1:]
        print(f'{partialShifted=}')

        freeTimes = tuple(
            B - A
            for (A, B) in zip(partialSums, partialShifted)
        )
        print(f'{freeTimes=}')

        return max(freeTimes)

# NOTE: Acceptance Rate 34.8% (medium)

# NOTE: Accepted on second Run (used [A, B] instead of B - A)
# NOTE: Accepted on first Submit
# NOTE: Runtime 221 ms Beats 5.32%
# NOTE: Memory 48.04 MB Beats 5.32%
