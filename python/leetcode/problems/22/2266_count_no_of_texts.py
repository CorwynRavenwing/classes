class Solution:
    def countTexts(self, pressedKeys: str) -> int:

        mod = 10 ** 9 + 7

        keypad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        encodings = {
            (key * (i + 1)): letter
            for key, letters in keypad.items()
            for i, letter in enumerate(letters)
        }
        # print(f'{encodings=}')

        possibleTexts = [0] * (len(pressedKeys) + 1)
        # possibleTexts[i] === possible texts that end at character #(i-1)
        # so PT[0] === 1 because "" is the only possible zero-length text 
        possibleTexts[0] = 1
        for I in range(0, len(possibleTexts) - 1):
            prior = possibleTexts[I]     # legal b/c i starts at 1
            # print(f'{i=} (pull {I}) {prior=}')
            # print(f'{I=} (pull {I})')
            # print(f'{I=}')
            for j in range(I, min(I + 5, len(possibleTexts) - 1)):
                frag = pressedKeys[I:j + 1]
                # print(f'  {j=} {frag=}')
                if frag in encodings:
                    # print(f'  {j=} "{frag}" -> "{encodings[frag]}" (push {j + 1})')
                    possibleTexts[j + 1] += prior   # might be the wrong bucket
                else:
                    # print(f'  {j=} "{frag}" -> no')
                    break
        # print(f'{possibleTexts=}')

        return possibleTexts[-1] % mod

