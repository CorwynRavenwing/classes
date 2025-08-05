class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        shiftEndpoints = [0] * (len(s) + 1)
        # print(f'start:\n  {shiftEndpoints=}')
        for (startI, endI, directionI) in shifts:
            # print(f'({startI=}, {endI=}, {directionI=})')
            if directionI == 1:
                shiftEndpoints[startI] += 1
                shiftEndpoints[endI + 1] -= 1
            else:
                shiftEndpoints[startI] -= 1
                shiftEndpoints[endI + 1] += 1
            # print(f'  {shiftEndpoints=}')
        # print(f'{shiftEndpoints=}')
        totalShifts = tuple(accumulate(shiftEndpoints))
        # print(f'{totalShifts=}')

        numbers = [
            alphabet.index(Letter)
            for Letter in s
        ]
        # print(f'{numbers=}')
        
        newNumbers = [
            (Number + Shift) % len(alphabet)
            for Number, Shift, in zip(numbers, totalShifts)
        ]
        # print(f'{newNumbers=}')
        
        newLetters = [
            alphabet[Number]
            for Number in newNumbers
        ]
        # print(f'{newLetters=}')

        newString = ''.join(newLetters)
        # print(f'{newString=}')

        return newString

# NOTE: Runtime 1003 ms Beats 83.23%
# NOTE: Memory 41.13 MB Beats 94.31%

# NOTE: re-ran for challenge:
# NOTE: Runtime 71 ms Beats 34.35%
# NOTE: Memory 42.00 MB Beats 7.90%
# NOTE: 93% speedup, 3x better percentage!
