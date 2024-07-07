class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:

        if upper + lower != sum(colsum):
            return []
        
        top = [None] * len(colsum)
        bot = [None] * len(colsum)
        # print(f'{upper=} {top=}\n{lower=} {bot=}')
        for i, C in enumerate(colsum):
            if C == 2:
                print(f'{i}: 1')
                top[i] = 1
                bot[i] = 1
                upper -= 1
                lower -= 1
                # print(f'{upper=} {top=}\n{lower=} {bot=}')

        for i, C in enumerate(colsum):
            if C == 0:
                print(f'{i}: 0')
                top[i] = 0
                bot[i] = 0
                upper -= 0
                lower -= 0
                # print(f'{upper=} {top=}\n{lower=} {bot=}')
                
        for i, C in enumerate(colsum):
            if C == 1:
                print(f'{i}: *')
                if upper:
                    top[i] = 1
                    bot[i] = 0
                    upper -= 1
                    lower -= 0
                elif lower:
                    top[i] = 0
                    bot[i] = 1
                    upper -= 0
                    lower -= 1
                else:
                    print(f'ran out of numbers {upper=} {lower=}')
                    return []
                # print(f'{upper=} {top=}\n{lower=} {bot=}')

        if None in top or None in bot:
            print(f'didnt fix all numbers {upper=} {lower=}')
            return []
        
        if upper < 0 or lower < 0:
            print(f'ran out of numbers {upper=} {lower=}')
            return []

        return [top, bot]

