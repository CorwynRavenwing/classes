class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        numbers = [
            alphabet.index(C)
            for C in s
        ]
        print(f'{numbers=}')
        print(f'{shifts=}')
        rShifts = reversed(shifts)
        rSums = [None] * len(s)
        for i, rS in enumerate(rShifts):
            if i == 0:
                rSums[i] = rS
            else:
                rSums[i] = rS + rSums[i - 1]
        Sums = tuple(reversed(rSums))
        print(f'{Sums=}')
        new_numbers = [
            (N + S) % 26
            for (N, S) in zip(numbers, Sums)
        ]
        print(f'{new_numbers=}')
        letters = [
            alphabet[N]
            for N in new_numbers
        ]
        print(f'{letters=}')

        return ''.join(letters)

