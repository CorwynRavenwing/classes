
    # this version gives the *length* of the subsequence:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @cache
        def DP(i: int, j: int) -> int:
            if -1 in (i,j):
                return 0
            # print(f'DP({i},{j})')
            if text1[i] == text2[j]:
                return DP(i - 1, j - 1) + 1
            else:
                return max([
                    DP(i - 1, j),
                    DP(i, j - 1),
                ])

        return DP(len(text1) - 1, len(text2) - 1)

    # this version gives the *value* of the subsequence:
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

