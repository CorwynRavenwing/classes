class Solution:
    def numDifferentIntegers(self, word: str) -> int:

        alpha = 'abcdefghijklmnopqrstuvwxyz'
        print(f'{word=}')
        for ch in alpha:
            if ch in word:
                word = word.replace(ch, ' ')
                print(f'{word=}')
        word = word.strip()
        print(f'{word=}')
        while '  ' in word:
            word = word.replace('  ', ' ')
            print(f'{word=}')
        strings = word.split(' ')
        print(f'{strings=}')
        numbers = (
            list(set(map(int, strings)))
            if strings != ['']
            else []
        )
        print(f'{numbers=}')
        return len(numbers)

