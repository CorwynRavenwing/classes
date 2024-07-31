class Solution:
    def smallestNumber(self, num: int) -> int:

        digitCounts = Counter(str(num))
        answerList = []
        if '-' in digitCounts:
            # NEGATIVE NUMBER: do everything backwards
            print(f'Negative')
            answerList.append('-')
            digitCounts['-'] -= 1
            # now search for all digits, in reverse order:
            for d in reversed(range(0, 10)):
                print(f'Try {d=}:')
                strD = str(d)
                if strD in digitCounts:
                    print(f'  Found {digitCounts[strD]}')
                    for i in range(digitCounts[strD]):
                        answerList.append(strD)
                    digitCounts[strD] = 0
        else:
            print(f'Positive')
            # search for a first digit that isn't a zero:
            for d in range(1, 10):
                print(f'Try {d=}:')
                strD = str(d)
                if strD in digitCounts:
                    print(f'  Found {digitCounts[strD]}; using {1}')
                    answerList.append(strD)
                    digitCounts[strD] -= 1
                    break
            # now search for all other digits, including a zero:
            for d in range(0, 10):
                print(f'Try {d=}:')
                strD = str(d)
                if strD in digitCounts:
                    print(f'  Found {digitCounts[strD]}')
                    for i in range(digitCounts[strD]):
                        answerList.append(strD)
                    digitCounts[strD] = 0
        print(f'{digitCounts=}')
        print(f'{answerList=}')
        return int(''.join(answerList))

