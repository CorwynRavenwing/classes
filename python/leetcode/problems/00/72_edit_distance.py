class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # SHORTCUT 1:
        # "delete from word1 or add to word1, to make it the same as word2"
        # is functionally equivalent to "delete from word1 or delete
        # from word2, to make them the same"

        # SHORTCUT 2:
        # "replace == delete and add" === "a delete from both strings
        # at the same time is only 1 point, not 2"
        
        # we borrow some code from #583:

        @cache
        def MD(i: int, j: int) -> int:
            nonlocal word1, word2
            try:
                A = word1[i]
            except IndexError:
                newJ = len(word2)   # skip entirety of other list
                return newJ - j
                
            try:
                B = word2[j]
            except IndexError:
                newI = len(word1)   # skip entirety of other list
                return newI - i

            if A == B:
                return 0 + MD(i + 1, j + 1)
            
            answers = []

            try:
                newI = word1.index(B, i)
                answers.append(
                    newI - i + MD(newI, j)  # skip to letter B in word 1
                )
            except ValueError:
                newI = len(word1)   # skip entirety of both remaining lists
                newJ = len(word2)
                answers.append(newI - i + newJ - j)

            try:
                newJ = word2.index(A, j)
                answers.append(
                    newJ - j + MD(i, newJ)  # skip to letter A in word 2
                )
            except ValueError:
                newI = len(word1)   # skip entirety of both remaining lists
                newJ = len(word2)
                answers.append(newI - i + newJ - j)

            answers.append(
                1 + MD(i + 1, j + 1)    # skip 1 letter in both: COUNTS AS 1 CHANGE
            )
            return min(answers)

        return MD(0, 0)

# NOTE: Kept 99.9% of the code from the example: changed only the
#       price of "skip 1 letter in both" from 2 to 1.
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 47 ms Beats 99.90%
# NOTE: Memory 17.48 MB Beats 92.78%
