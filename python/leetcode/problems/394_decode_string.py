class Solution:
    def decodeString(self, s: str) -> str:
        LEFT = '['
        RIGHT = ']'
        work = list(s)
        while RIGHT in work:
            print(f'{work=}')
            rightIndex = work.index(RIGHT)
            i = rightIndex
            print(f'{rightIndex=}')
            while i >= 0 and work[i] != LEFT:
                print(f'seek left: [{i}]={work[i]}')
                i -= 1
            leftIndex = i
            i -= 1
            print(f'back: [{i}]={work[i]}')
            while i >= 0 and work[i].isdigit():
                print(f'seek digit: [{i}]={work[i]}')
                i -= 1
            numberIndex = i + 1
            number = int(''.join(work[numberIndex:leftIndex]))
            string = ''.join(work[leftIndex+1:rightIndex])
            newString = string * number
            print(f'{number} * "{string}" = "{newString}"')
            print(f'replace={work[numberIndex:rightIndex+1]}')
            work[numberIndex:rightIndex+1] = [newString]

        print(f'{work=}')

        return ''.join(work)

