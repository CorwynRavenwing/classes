class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:

        # We reuse some code from #2865 ... and it completely doesn't work.
        # Time Limit Exceeded because the data limits are so much higher.
        # We will need to create a much more efficient algorithm.

        def createMountainCounts(H: List[int]) -> List[int]:
            # print(f'createMountainCounts({H}):')
            answer = [None] * len(H)
            answer[0] = Counter([H[0]])
            # print(f'  {0:} {answer[0]}')
            for i in range(1, len(H)):
                C = Counter([H[i]])
                # print(f'  Move counter data')
                for value, count in answer[i - 1].items():
                    newValue = min(value, H[i])
                    # print(f'    {newValue} = min({value}, {H[i]})')
                    C[newValue] += count
                answer[i] = C
                # print(f'  {i:} {answer[i]}')
            # print(f'{answer=}')
            totals = [
                sum([
                    height * count
                    for height, count in C.items()
                ])
                for C in answer
            ]
            # print(f'{totals=}')
            return totals
        
        REV = lambda x: tuple(reversed(tuple(x)))

        mountainCountsUpwards = createMountainCounts(maxHeights)
        # print(f'{mountainCountsUpwards=}')

        mountainCountsDownwards = REV(
            createMountainCounts(
                REV(
                    maxHeights
                )
            )
        )
        # print(f'{mountainCountsDownwards=}')

        answers = [
            CountUp + CountDown - H     # subtract H b/c it is counted in both CU and CD
            for (index, H, CountUp, CountDown) in zip(
                count(),
                maxHeights,
                mountainCountsUpwards,
                mountainCountsDownwards
            )
        ]
        # print(f'{answers=}')
        return max(answers)

# NOTE: a much much better algorithm ... that still TLE for big inputs
