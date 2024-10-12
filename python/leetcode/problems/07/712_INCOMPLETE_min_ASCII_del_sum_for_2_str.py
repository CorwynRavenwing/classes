class Solution:

    def cheapestCommonSubsequence(self, text1: str, text2: str) -> int:

        @cache
        def DP(i: int, j: int) -> int:
            if (i == -1) and (j == -1):
                return 0
            if (i == -1):
                B = text2[j]
                print(f'DP({i},{j})"-{B}":')
                skip_J = DP(i, j - 1)
                answer_B = ord(B) + skip_J
                print(f'DP({i},{j})"-{B}":{B}: {ord(B)} + {skip_J} = {answer_B}')
                return ord(B) + skip_J
            if (j == -1):
                A = text1[i]
                print(f'DP({i},{j})"{A}-":')
                skip_I = DP(i - 1, j)
                answer_A = ord(A) + skip_I
                print(f'DP({i},{j})"{A}-":{A}: {ord(A)} + {skip_I} = {answer_A}')
                return ord(A) + skip_I

            A = text1[i]
            B = text2[j]
            print(f'DP({i},{j})"{A}{B}":')
            if A == B:
                print(f'DP({i},{j})"{A}{B}": Skip "{A}={B}" $0')
                return DP(i - 1, j - 1) + 1
            else:
                skip_I = DP(i - 1, j)
                skip_J = DP(i, j - 1)
                answer_A = ord(A) + skip_I
                answer_B = ord(B) + skip_J
                print(f'DP({i},{j})"{A}{B}":{A}: {ord(A)} + {skip_I} = {answer_A}')
                print(f'DP({i},{j})"{A}{B}":{B}: {ord(B)} + {skip_J} = {answer_B}')
                answer = min([
                    answer_A,
                    answer_B,
                ])
                print(f'DP({i},{j})"{A}{B}":X: {answer}')
                return answer

        return DP(len(text1) - 1, len(text2) - 1)

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        return self.cheapestCommonSubsequence(s1, s2)

# NOTE: this version also gives incorrect answers.  I'll return
#       to this later
