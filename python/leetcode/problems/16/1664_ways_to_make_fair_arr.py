class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
        # INSIGHT: the "odd indexes" and "even indexes" in the answer
        # correspond to "odd indexes prior to the chosen one, plus even indexes after"
        # and the reverse.

        DEBUG = False

        Even = [
            N
            for index, N in enumerate(nums)
            if index % 2 == 0
        ]
        Odds = [
            N
            for index, N in enumerate(nums)
            if index % 2 != 0
        ]
        if DEBUG: print(f'{Even=}')
        if DEBUG: print(f'{Odds=}')

        ACC = lambda X: (0,) + tuple(accumulate(X))
        accEven = ACC(Even)
        accOdds = ACC(Odds)
        if DEBUG: print(f'{accEven=}')
        if DEBUG: print(f'{accOdds=}')

        answer = 0

        for i in range(len(nums)):
            is_even = (i % 2 == 0)
            index = i // 2
            if DEBUG: print(f'{i=} {is_even=} {index=}')

            index_plus_1_if_odd = sum([
                index,
                (0 if is_even else 1)
            ])
            leftEvenStart = 0
            leftEvenStop = index_plus_1_if_odd
            leftOddStart = 0
            leftOddStop = index
            rightEvenStart = index_plus_1_if_odd
            rightEvenStop = len(Odds)
            rightOddStart = index + 1
            rightOddStop = len(Even)

            if DEBUG: print(f'  Even: e{leftEvenStart}-{leftEvenStop} + o{rightEvenStart}-{rightEvenStop}')
            evenSumLeft = accEven[leftEvenStop] - accEven[leftEvenStart]
            evenSumRight = accOdds[rightEvenStop] - accOdds[rightEvenStart]
            evenSum = evenSumLeft + evenSumRight
            if DEBUG: print(f'    {evenSum} = {evenSumLeft} + {evenSumRight}')

            if DEBUG: print(f'  Odds: o{leftOddStart}-{leftOddStop} + e{rightOddStart}-{rightOddStop}')
            oddSumLeft = accOdds[leftOddStop] - accOdds[leftOddStart]
            oddSumRight = accEven[rightOddStop] - accEven[rightOddStart]
            oddSum = oddSumLeft + oddSumRight
            if DEBUG: print(f'    {oddSum} = {oddSumLeft} + {oddSumRight}')

            fair = (evenSum == oddSum)
            if DEBUG: print(f'      {fair=} = ({evenSum} == {oddSum})')
            
            if fair:
                answer += 1

        return answer

# NOTE: Accepted on second Run (variable name typos)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 434 ms Beats 6.20%
# NOTE: Memory 26.24 MB Beats 20.17%
