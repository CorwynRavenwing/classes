class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        # Hint 1: by column, find number of consecutive 1's ending at each position
        invMatrix = tuple(zip(*matrix))
        print(f'{invMatrix=}')
        ACCZERO = lambda a, b: (a + 1 if b else b)
        invPartialSum = [
            tuple(accumulate(col, ACCZERO))
            for col in invMatrix
        ]
        print(f'{invPartialSum=}')

        # hint 2a: by row, sort cumulative values in (non-strictly) decreasing order
        partialSum = tuple(zip(*invPartialSum))
        print(f'{partialSum=}')
        sortedPartialSum = [
            tuple(sorted(row, reverse=True))
            for row in partialSum
        ]
        print(f'{sortedPartialSum=}')
        firstRow = sortedPartialSum[0]
        firstCol = [
            row[0]
            for row in sortedPartialSum
        ]
        print(f'{firstRow=}')
        print(f'{firstCol=}')

        # hint 2b: "fit" the largest submatrix.  Not a hint in English.

        max_answer = 0
        for phase, digits in enumerate([firstRow, firstCol]):
            L = 0
            R = 0
            min_sum = float('+inf')
            while 0 <= L <= R <= len(digits):
                try:
                    A = digits[R]
                except IndexError:
                    A = 0
                R += 1
                # at this point, min_sum === min(digits[L:R])
                min_sum = min(A, min_sum)
                answer = min_sum * (R - L)
                max_answer = max(answer, max_answer)
                print(f'{phase}:[{L}:{R}]: {A=} {min_sum=} {answer=} {max_answer=}')
                # print(f'  DEBUG: {digits[L:R]};')
                # print(f'  DEBUG: {min_sum} * ({R}-{L})')
                # print(f'       = {min_sum} * ({R-L})')
                # print(f'       = {answer}')
                if min_sum == 0:
                    L += 1
                    R = L
                    min_sum = float('+inf')
                    continue

        return max_answer

# NOTE: gets the wrong answer for complex inputs, e.g. test case #6
