class Solution:
    def flowerGame(self, n: int, m: int) -> int:

        # SHORTCUT:
        # the "clockwise / anticlockwise" thing doesn't matter, b/c there is
        # no pentalty for running out of flowers in one direction, only in both.

        # SHORTCUT:
        # Every turn, Alice picks 1 flower (somewhere), Bob picks 1 flower (somewhere).
        # On every pair of turns, the total number of flowers goes down by 2.
        # If the total number of flowers is zero [Edit: AFTER] Alice's turn, she wins.
        # Therefore, Alice wins if the starting total number of flowers is [Edit: ODD].

        # SHORTCUT:
        # the number of *pairs* in the range (1..n, 1..m) is (n * m).
        # the number of *ODD total* pairs is (n * m) / 2, rounded DOWN for odd n*m.

        # Therefore we just do an integer division:
        return (n * m) // 2

# NOTE: Yes, 20 lines of explanation for 1 line of code.
# NOTE: Accepted on first Submit
# NOTE: Runtime 38 ms Beats 45.63%
# NOTE: O(1)
# NOTE: Memory 16.46 MB Beats 73.13%
# NOTE: O(1)
