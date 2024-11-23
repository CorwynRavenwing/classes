class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:

        # SHORTCUT: this question is exactly equivalent to the following:
        # "find the length(cardPoints) - k sequential elements with the
        # *minimum* total sum.  Return sum(cardPoints) - this sum."
        # this allows us to proceed in O(N) without recursion.

        Len = len(cardPoints) - k
        I = 0
        J = I + Len
        Total = sum(cardPoints[I:J])
        MinTotal = Total

        while 0 <= I < J <= len(cardPoints):
            MinTotal = min(Total, MinTotal)
            try:
                Total -= cardPoints[I]
                Total += cardPoints[J]
            except IndexError:
                break
            I += 1
            J += 1

        return sum(cardPoints) - MinTotal

# NOTE: new version which solves a much easier, equivalent problem
# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (fencepost error)
# NOTE: Runtime 30 ms Beats 43.00%
# NOTE: Memory 27.12 MB Beats 60.89%
