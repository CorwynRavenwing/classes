class Solution:
    def findLatestTime(self, s: str) -> str:

        print(f'{s=}')
        L = list(s)
        print(f'  {L=}')
        while '?' in L:
            index = L.index('?')
            if index == 0:
                if L[1] in ['?', '0', '1']:
                    L[index] = '1'
                else:
                    L[index] = '0'
            elif index == 1:
                if L[0] == '1':
                    L[index] = '1'
                else:
                    L[index] = '9'
            elif index == 2:
                L[index] = ':'
            elif index == 3:
                L[index] = '5'
            elif index == 4:
                L[index] = '9'
            else:
                raise Exception(f'Invalid index of "?": {s=} {index=}')
            print(f'  {L=}')
        s = ''.join(L)
        return s

