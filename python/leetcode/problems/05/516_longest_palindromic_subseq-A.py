class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        DEBUG = False

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

# NOTE: either Time Limit Exceeded or Memory Limit Exceeded,
#       depending on what we do and don't try caching.
