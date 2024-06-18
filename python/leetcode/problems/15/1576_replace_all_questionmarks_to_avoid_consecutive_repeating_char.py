class Solution:
    def modifyString(self, s: str) -> str:
        sList = ['_'] + list(s) + ['_']
        while '?' in sList:
            print(f"{sList}")
            index = sList.index('?')
            group = sList[index-1:index+2]
            print(f"  {group}")
            letter = 'a'
            if letter in group:
                letter = 'b'
            if letter in group:
                letter = 'c'
            if letter in group:
                raise Exception(f"Invalid group {group} contains all of a,b,c")
            sList[index] = letter
            print(f"    '{letter}'")
        ignore = (sList.pop(0), sList.pop(-1))
        return ''.join(sList)

