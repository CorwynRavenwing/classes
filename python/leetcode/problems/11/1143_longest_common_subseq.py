class Solution:
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

# NOTE: Accepted on first Submit
# NOTE: Runtime 1167 ms Beats 13.93%
# NOTE: Memory 309.98 MB Beats 7.30%
