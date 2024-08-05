class Solution:
    def largestPalindromic(self, num: str) -> str:

        digitCounts = Counter(num)
        print(f'{digitCounts=}')

        frontEnd = ''
        middle = ''
        # backEnd = ''  # === frontEnd backwards

        for (digit, count) in sorted(digitCounts.items(), reverse=True):
            while count >= 2:
                if digit == '0' and frontEnd == '':
                    print(f'No leading zeros')
                    break
                print(f'+2 {digit}')
                frontEnd += digit
                count -= 2
            if count and middle == '':
                print(f'+1 {digit}')
                middle = digit
                count -= 1
        backEnd = ''.join(
            reversed(frontEnd)
        )
        print(f'{frontEnd=} {middle=} {backEnd=}')
        return frontEnd + middle + backEnd
# NOTE: Runtime 137 ms Beats 13.29%
# NOTE: Memory 18.33 MB Beats 23.63%
