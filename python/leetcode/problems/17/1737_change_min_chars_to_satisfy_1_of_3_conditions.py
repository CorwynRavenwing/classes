class Solution:
    def minCharacters(self, a: str, b: str) -> int:

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        def make_all_LE_price(compareLetter: str, letterCounts: Counter) -> int:
            return sum([
                count
                for letter, count in letterCounts.items()
                if letter > compareLetter
            ])

        def make_all_GT_price(compareLetter: str, letterCounts: Counter) -> int:
            return sum([
                count
                for letter, count in letterCounts.items()
                if letter <= compareLetter
            ])

        def condition_LE_GT_price(LE: str, GT: str) -> int:
            nonlocal alphabet
            LE_counts = Counter(LE)
            GT_counts = Counter(GT)
            return min([
                sum([
                    make_all_LE_price(compareLetter, LE_counts),
                    make_all_GT_price(compareLetter, GT_counts),
                ])
                for compareLetter in alphabet
                if compareLetter != 'z'
            ])
            
        def condition_1_price() -> int:
            nonlocal a, b
            return condition_LE_GT_price(a, b)

        def condition_2_price() -> int:
            nonlocal a, b
            return condition_LE_GT_price(b, a)

        def condition_3_price() -> int:
            letterCount = Counter(a + b)
            print(f'{letterCount=}')
            max_count = max(letterCount.values())
            max_letter = [
                letter
                for letter, count in letterCount.items()
                if count == max_count
            ]
            max_letter = max_letter[0]
            print(f'{max_count=} {max_letter=}')
            price = sum([
                count
                for letter, count in letterCount.items()
                if letter != max_letter
            ])
            print(f'{price=}')
            return price

        return min(
            condition_1_price(),
            condition_2_price(),
            condition_3_price(),
        )

