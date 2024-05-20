# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        L = 0   # guaranteed lower than 1..n
        R = n+1 # guaranteed higher than 1..n
        while True:
            M = (L + R) // 2
            print(f'[{L},{M},{R}]')
            answer = guess(M)
            if answer == 0:
                print(f'found {M}')
                return M
            elif answer == -1:
                print(f'{M} is too high')
                R = M
            elif answer == 1:
                print(f'{M} is too low')
                L = M
        return -999

