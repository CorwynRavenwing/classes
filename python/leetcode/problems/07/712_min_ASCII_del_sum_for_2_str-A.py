class Solution:

    # SHORTCUT: it asks for "the lowest ASCII sum of deleted characters"
    # as though we had a choice ... but to make two strings equal, I'm
    # expecting us to always be deleting the minimum *count* of characters
    # b/c the ASCII values of "a" and "z" are (A) high numbers
    # and (B) near each other.

    def longestCommonSubsequence(self, text1: str, text2: str) -> str:

        @cache
        def DP(i: int, j: int) -> int:
            if -1 in (i,j):
                return ''
            print(f'DP({i},{j})')
            if text1[i] == text2[j]:
                return DP(i - 1, j - 1) + text1[i]
            else:
                answers = [
                    DP(i - 1, j),
                    DP(i, j - 1),
                ]
                maxLen = max(map(len, answers))
                matchingAnswers = [
                    A
                    for A in answers
                    if len(A) == maxLen
                ]
                answer = matchingAnswers[0]
                return answer

        return DP(len(text1) - 1, len(text2) - 1)

    def subtractStrings(self, sOrig, sMinus) -> str:
        # 'ABCDE' - 'AD' = 'BCE'
        answer = ''
        for char in sOrig:
            if sMinus and sMinus[0] == char:
                sMinus = sMinus[1:]
                continue
            answer += char
        return answer
    
    def score(self, s: str) -> int:
        return sum([
            ord(char)
            for char in s
        ])

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        common = self.longestCommonSubsequence(s1, s2)
        print(f'{common=}')
        x1 = self.subtractStrings(s1, common)
        x2 = self.subtractStrings(s2, common)
        print(f'{x1=} {x2=}')

        return self.score(x1) + self.score(x2)

# NOTE: when there are more than one possible resultant string
#       of the same length, this version sometimes chooses
#       the wrong one
