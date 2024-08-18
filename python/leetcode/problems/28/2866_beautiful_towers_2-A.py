class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:

        # We reuse some code from #2865 ... and it completely doesn't work.
        # Time Limit Exceeded because the data limits are so much higher.
        # We will need to create a much more efficient algorithm.

        @cache
        def mountainSumUpwards(index: int, maxValue: int) -> int:
            if index >= len(maxHeights):
                return 0
            # print(f'mountainSumUpwards({index},{maxValue})')
            thisValue = min(maxHeights[index], maxValue)
            return thisValue + mountainSumUpwards(index + 1, thisValue)

        @cache
        def mountainSumDownwards(index: int, maxValue: int) -> int:
            if index < 0:
                return 0
            # print(f'mountainSumDownwards({index},{maxValue})')
            thisValue = min(maxHeights[index], maxValue)
            return thisValue + mountainSumDownwards(index - 1, thisValue)

        answers = [
            sum([
                mountainSumDownwards(peakIndex - 1, peakHeight),
                peakHeight,
                mountainSumUpwards(peakIndex + 1, peakHeight),
            ])
            for peakIndex, peakHeight in enumerate(maxHeights)
        ]
        
        # print(f'{answers=}')
        return max(answers)
# NOTE: this fixed the Time Limit Exceeded and replaced it with
#       a Memory Limit Exceeded instead :-(
