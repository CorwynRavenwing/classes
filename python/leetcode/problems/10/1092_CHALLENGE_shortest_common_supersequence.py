class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> str:

        @cache
        def DP(i: int, j: int) -> int:
            if -1 in (i,j):
                return ''
            # print(f'DP({i},{j})')
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

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        M = len(str1)
        N = len(str2)

        # def answer_i_j(i: int, j: int) -> str:
        #     answer = ""
        #     A = str1[:i]
        #     B = str2[:j]
        #     lcss = self.longestCommonSubsequence(A, B)
        #     print(f'[{i},{j}]: "{A}" "{B}" -> "{lcss}"')
        #     return len(lcss)

        # dp = [
        #     [0] * (N + 1)
        #     for _ in range(M + 1)
        # ]
        # # print(f'{dp=}')
        # for i in range(M + 1):
        #     for j in range(N + 1):
        #         dp[i][j] = answer_i_j(i, j)
        # print(f'{dp=}')

        # answer = []

        # before figuring out the preceeding, I'll try my naive idea
        # and see whether it works.

        answer = []
        lcss = self.longestCommonSubsequence(str1, str2)
        # make strings mutable
        str1 = list(str1)
        str2 = list(str2)
        lcss = list(lcss)
        while str1 or str2 or lcss:
            print(f'LOOP: {str1=} {str2=} {lcss=}')
            while str1 and lcss and str1[0] != lcss[0]:
                A = str1.pop(0)
                print(f'Add {A=} from str1')
                answer.append(A)
            while str2 and lcss and str2[0] != lcss[0]:
                B = str2.pop(0)
                print(f'Add {B=} from str2')
                answer.append(B)
            while str1 and str2 and lcss and str1[0] == str2[0] == lcss[0]:
                A = str1.pop(0)
                B = str2.pop(0)
                C = lcss.pop(0)
                print(f'Add {C=} from LCS')
                answer.append(C)
            if not lcss:
                answer.extend(str1)
                answer.extend(str2)
                str1 = []
                str2 = []

        return ''.join(answer)

# NOTE: Acceptance Rate 59.8% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 1924 ms Beats 5.01%
# NOTE: Memory 295.52 MB Beats 12.72%
