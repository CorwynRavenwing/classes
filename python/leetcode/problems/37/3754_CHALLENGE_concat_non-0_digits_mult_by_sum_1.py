class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
        nonZeroDigits = [
            D
            for D in str(n)
            if D != '0'
        ]
        # print(f'{nonZeroDigits=}')
        concatted = ''.join(nonZeroDigits)
        if concatted == '':
            return 0
        concatted = int(concatted)
        print(f'{concatted=}')
        summed = sum([
            int(D)
            for D in nonZeroDigits
        ])
        print(f'{summed=}')

        return summed * concatted

# NOTE: Acceptance Rate 56.1% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.30 MB Beats 51.25%
