class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        DEBUG = False

        K = len(nums)
        Data = sorted([
            (val, listNum)
            for listNum, values in enumerate(nums)
            for val in values
        ])
        # print(f'{Data=}')
        answerLength = float('+inf')
        answer = []
        L = 0
        R = 0
        (val, listNum) = Data[R]
        A = val
        B = val
        listCount = Counter([listNum])
        while True:
            if DEBUG: print(f'[{L},{R}]({A},{B}): {answerLength}:{answer} {listCount}')
            if len(listCount) < K:
                if DEBUG: print(f'  No: expand to right')
                R += 1
                try:
                    (val, listNum) = Data[R]
                    B = val
                except IndexError:
                    if DEBUG: print(f'  Out of numbers')
                    break
                listCount[listNum] += 1
                continue
            else:
                if DEBUG: print(f'  Yes: answer [{A},{B}]; contract from left')
                thisLength = B - A
                if answerLength > thisLength:
                    answerLength = thisLength
                    answer = [A,B]
                else:
                    if DEBUG: print(f'    (not answer: {thisLength=} >= {answerLength})')
                (val, listNum) = Data[L]
                listCount[listNum] -= 1
                if not listCount[listNum]:
                    del listCount[listNum]
                L += 1
                try:
                    (val, listNum) = Data[L]
                except IndexError:
                    if DEBUG: print(f'  Out of numbers')
                    break
                A = val
                continue

        return answer

# NOTE: Acceptance Rate 63.7% (HARD)
# NOTE: Runtime 186 ms Beats 80.56%
# NOTE: Memory 25.41 MB Beats 5.75%
