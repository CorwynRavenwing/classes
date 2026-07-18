class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:

        # NOTE: The code from part 1: will not work here
        
        # def sumAndMultiply(self, n: int) -> int:
        
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

# NOTE: Acceptance Rate 24.8% (medium)
