class Solution:

    # we borrow some code from #1143:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        DEBUG = False

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


        # caches:
        # no, no: Time Limit Exceeded
        # yes, no: Time Limit Exceeded
        # no, yes: Time Limit Exeeded
        # yes, yes: Memory Limit Exceeded
        # ... well *that's* un-helpful

        # @cache
        def stringFoundReversedInSAfterIndex(needle: str, index: int) -> bool:
            if DEBUG: print(f'SFRISAI("{needle}",{index})')
            # nonlocal s
            if not needle:
                return True
            lastChar = needle[-1]       # searching for string *reversed*
            restOfNeedle = needle[:-1]
            try:
                nextIndex = s.index(lastChar, index + 1)
            except ValueError:
                return False
            return stringFoundReversedInSAfterIndex(restOfNeedle, nextIndex)
        
        @cache
        def DP(stringSoFar: str, index: int) -> int:
            if DEBUG: print(f'DP("{stringSoFar}",{index})')
            nextIndex = index + 1
            LEN = len(stringSoFar)
            truncated = stringSoFar[:-1]
            try:
                newString = stringSoFar + s[index]
            except IndexError:
                # there is no "next character" to pick or not-pick:
                return 0
            NEW_LEN = LEN + 1
            newTruncated = stringSoFar

            # DON'T PICK:
            if stringFoundReversedInSAfterIndex(stringSoFar, index):
                # "ABC" + "CBA"
                dont_pick = max(
                    LEN * 2,
                    DP(stringSoFar, nextIndex)
                )
            elif stringFoundReversedInSAfterIndex(truncated, index):
                # "ABC" + "BA"
                dont_pick = max(
                    LEN * 2 - 1,
                    DP(stringSoFar, nextIndex)
                )
            else:
                dont_pick = 0

            # DO PICK:
            if stringFoundReversedInSAfterIndex(newString, index):
                # "ABCD" + "DCBA"
                do_pick = max(
                    NEW_LEN * 2,
                    DP(newString, nextIndex)
                )
            elif stringFoundReversedInSAfterIndex(newTruncated, index):
                # "ABCD" + "CBA"
                do_pick = max(
                    NEW_LEN * 2 - 1,
                    DP(newString, nextIndex)
                )
            else:
                do_pick = 0

            return max(dont_pick, do_pick)

        return DP('', 0)

    def longestPalindromeSubseq(self, s: str) -> int:

        # SHORTCUT: a palindrome is a sequence that is the same
        # backwards and forwards.  Therefore the longest palindromic
        # sequence of a string, is the longest common subsequence
        # between the string itself, and its reverse.

        REV = lambda x: tuple(reversed(tuple(x)))

        return self.longestCommonSubsequence(
            s,
            REV(s)
        )

# NOTE: re-used all of prior version plus a bit of glue code
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 1708 ms Beats 10.05%
# NOTE: Memory 530.88 MB Beats 5.12%
