class Solution:
    def minimumPushes(self, word: str) -> int:
        
        def encodePushes(word: str, mapping: Dict[str, str]) -> List[str]:
            # mapping = {
            #     '2': 'abc',
            #     '3': 'def',
            #     # ... etc.
            # }
            reverseMapping = {
                char: button * (index + 1)
                for button, charList in mapping.items()
                for index, char in enumerate(charList)
            }
            print(f'{reverseMapping=}')
            return [
                reverseMapping[char]
                for char in word
            ]

        def findPrice(word: str, mapping: Dict[str, str]) -> int:
            pushes = encodePushes(word, mapping)
            print(f'{pushes=}')
            return sum(
                map(
                    len,
                    pushes
                )
            )
        
        # defaultMapping = {
        #     '2': 'abc',
        #     '3': 'def',
        #     '4': 'ghi',
        #     '5': 'jkl',
        #     '6': 'mno',
        #     '7': 'pqrs',
        #     '8': 'tuv',
        #     '9': 'wxyz',
        # }

        # return findPrice(word, defaultMapping)

        wordCounts = Counter(word)
        print(f'{wordCounts=}')
        lettersByFrequency = [
            letter
            for letter, count in sorted(
                wordCounts.items(),     # take letters and frequencies
                key=lambda x: x[1],     # sort by frequency
                reverse=True            # ... descending
            )
        ]
        print(f'{lettersByFrequency=}')
        allowed_buttons = '23456789'
        button_index = 0
        mapping = {}
        for letter in lettersByFrequency:
            button = allowed_buttons[button_index]
            print(f'map {letter} to {button}')
            mapping.setdefault(button, '')
            mapping[button] += letter
            button_index += 1
            button_index %= len(allowed_buttons)
        print(f'{mapping=}')

        return findPrice(word, mapping)

