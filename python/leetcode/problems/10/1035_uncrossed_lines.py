class Solution:
        
        # SHORTCUT: the pairings produced by uncrossed lines form a
        # shared sub-sequence.  Allowing rearrangement would instead
        # find a shared sub-*array*, which is a completely different thing.

        # So we use the Longest Common Sub-Sequence code we already have.

    # this version gives the *length* of the subsequence:
    def longestCommonSubsequence(self, text1: List[int], text2: List[int]) -> int:

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

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        return self.longestCommonSubsequence(nums1, nums2)

# NOTE: re-used complete prior version with glue code and type change
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 247 ms Beats 20.27%
# NOTE: Memory 60.61 MB Beats 15.14%
