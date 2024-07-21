class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:

        digits_improve = [
            (
                '+'
                if (newValue > index)
                else '='
                if (newValue == index)
                else '-'
            )
            for index, newValue in enumerate(change)
        ]
        # print(f'{digits_improve=}')

        changes_improve = [
            digits_improve[int(digit)]
            for digit in num
        ]
        print(f'{changes_improve=}')

        if '+' not in changes_improve:
            print(f'No improvements possible')
            return num
        
        first_change = changes_improve.index('+')
        if '-' in changes_improve[first_change:]:
            last_change = changes_improve.index('-', first_change)
        else:
            last_change = len(changes_improve)
        
        print(f'Changing from {first_change} to {last_change}:')
        new_num = [
            (
                str(change[int(digit)])
                if first_change <= index < last_change
                else digit
            )
            for index, digit in enumerate(num)
        ]
        print(f'{new_num=}')
        return ''.join(new_num)

