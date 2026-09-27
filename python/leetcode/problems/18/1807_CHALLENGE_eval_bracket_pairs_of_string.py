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

# NOTE: Acceptance Rate 70.2% (medium)

# NOTE: re-ran for challenge:
# NOTE: Runtime 6861 ms Beats 5.30%
# NOTE: Memory 51.27 MB Beats 97.82%
