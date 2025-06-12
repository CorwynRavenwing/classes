class Solution:
    def clearStars(self, s: str) -> str:

        if '*' not in s:
            return s
        
        s = list(s)     # make it mutable
        
        indexesByCharacter = {}
        Characters = set()
        
        for (index, C) in enumerate(s):
            if C != '*':
                # normal character: insert.
                indexesByCharacter.setdefault(C, [])
                bisect.insort(indexesByCharacter[C], index)
                Characters.add(C)
                # print(f'{C} -> push')
            else:
                # asterisk: pop nearest minimum character
                s[index] = 'X'
                C = min(Characters)
                # print(f'(*) -> pop {C}')
                indexes = indexesByCharacter[C]
                index = indexes.pop(-1)     # last (right-most) one
                check = s[index]
                if check != C:
                    print(f'  ERROR!  {index=} {check=} {C=}')
                    return -77777
                s[index] = 'X'
                if not indexes:
                    print(f'  No more {C} in stack.')
                    del indexesByCharacter[C]
                    Characters.remove(C)
        answer = [
            C
            for C in s
            if C != 'X'
        ]
        # print(f'{answer=}')
        return ''.join(answer)

# NOTE: Runtime 679 ms Beats 41.93%
# NOTE: Memory 20.44 MB Beats 99.31%

# NOTE: re-ran for challenge:
# NOTE: Runtime 691 ms Beats 35.97%
# NOTE: Memory 21.73 MB Beats 97.12%
