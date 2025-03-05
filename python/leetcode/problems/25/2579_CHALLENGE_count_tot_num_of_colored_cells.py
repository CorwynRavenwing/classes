class Solution:
    def coloredCells(self, n: int) -> int:
        
        # SHORTCUT: Imagine the grid at N = 4:
        #
        # _ _ _ A _ _ _
        # _ _ B A A _ _
        # _ B B A A A _
        # B B B A A A A
        # _ D D C C C _
        # _ _ D C C _ _
        # _ _ _ C _ _ _

        # Take sections A and B, turn B around, and combine:
        # A B B B
        # A A B B
        # A A A B
        # A A A A
        # This is a square of area N^2.

        # Similarly combine sections C and D:
        # C C C
        # C C D
        # C D D
        # This is a square of area (N-1)^2.

        return n*n + (n-1)*(n-1)
        # Yes, 1 line of code and 21 lines of comment about it

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.80 MB Beats 48.12%
