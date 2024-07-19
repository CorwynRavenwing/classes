class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:

        # kDict = dict(knowledge)
        # print(f'{kDict=}')

        # print(f'{s=}')
        for (key, value) in knowledge:
            keyInParens = f'({key})'
            s = s.replace(keyInParens, value)
            # print(f'{s=}')
        
        while '(' in s:
            indexLeft = s.index('(')
            indexRight = s.index(')')
            s = s[:indexLeft] + '?' + s[indexRight + 1:]
            # print(f'{s=}')

        return s

