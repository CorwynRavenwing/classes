class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        
        mod = 10 ** 9 + 7

        digits = tuple(map(int, num))
        print(f'{digits=}')
        
        size = len(digits)
        counts = Counter(digits)
        total = sum(digits)
        if total % 2 != 0:
            print(f'Odd {total=}: impossible')
            return 0
        half = total // 2
        print(f'{size=} {total=} {half=} {counts=}')

        @cache
        def DP(digit, oddCount, evenCount, remainingSum):
            # print(f'DP({digit},{oddCount},{evenCount},{remainingSum})')
            if oddCount == evenCount == remainingSum == 0:
                # all numbers used, and string is balanced
                return 1

            if digit < 0 or oddCount < 0 or evenCount < 0:
                # overflow error. No possible strings.
                return 0
            
            answer = 0
            digit_count = counts[digit]
            for oddIndexes in range(digit_count + 1):
                evenIndexes = digit_count - oddIndexes

                comb_odd = comb(oddCount, oddIndexes)
                comb_even = comb(evenCount, evenIndexes)

                # arbitrarily choose odd indexes to subtract
                sumOddUsed = digit * oddIndexes
                newRemainingSum = remainingSum - sumOddUsed

                recurse = DP(
                    digit - 1,
                    oddCount - oddIndexes,
                    evenCount - evenIndexes,
                    newRemainingSum,
                )

                result = comb_odd * comb_even * recurse

                answer += result
            
            return answer % mod
        
        evenDigits = size // 2
        oddDigits = size - evenDigits   # might have an extra

        answer = DP(
            9,      # start at digit '9' and work down
            oddDigits,
            evenDigits,
            half,
        )

        return answer % mod

# NOTE: Acceptance Rate 18.4% (HARD)

# NOTE: Accepted on third Run (typos and logic errors)
# NOTE: Accepted on third Submit (Output Exceeded)
# NOTE: Runtime 1839 ms Beats 46.55%
# NOTE: Memory 183.54 MB Beats 15.52%
