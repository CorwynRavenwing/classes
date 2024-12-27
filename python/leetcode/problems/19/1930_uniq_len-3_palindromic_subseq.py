class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        indexesByValue = {}
        for index, value in enumerate(s):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        # print(f'{indexesByValue=}')

        # There are 26 letters.  Worst-case this code is O(26*26)
        answerSet = set()
        for outerLetter, indexes in indexesByValue.items():
            if len(indexes) <= 1:
                print(f'{outerLetter}: no')
                continue
            print(f'{outerLetter}:')
            seen = set()
            A = indexes[0]
            B = indexes[-1]
            if B - A <= 1:
                print(f'  {A},{B}: no')
                continue
            print(f'  {A},{B}:')
            frag = s[A + 1:B]
            fragSet = set(frag) - seen
            seen |= fragSet
            # print(f'    DEBUG: {frag=} {fragSet=}')
            for middleLetter in fragSet:
                palindrome = outerLetter + middleLetter + outerLetter
                print(f'    +{palindrome}')
                answerSet.add(palindrome)
        
        print(f'{answerSet=}')

        return len(answerSet)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 162 ms Beats 78.16%
# NOTE: Memory 22.96 MB Beats 5.06%
