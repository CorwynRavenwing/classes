class Solution:

    def minDistance(self, word1: str, word2: str) -> int:

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
                2 + MD(i + 1, j + 1)    # skip 1 letter in both
            )
            return min(answers)

        return MD(0, 0)

# NOTE: Accepted on first Submit (with this version)
# NOTE: Runtime 203 ms Beats 18.22%
# NOTE: Memory 21.06 MB Beats 15.99%
