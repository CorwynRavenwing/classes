class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        
        # legal combinations:
        # AA BB
        # AB AA
        # AB AB
        # BB AA
        # BB AB

        # invalid combinations:
        # AA AA(
        # AA AB
        # AB BB
        # BB BB

        # therefore, the max length is:
        # if X = Y: everything
        # if X > Y: all of Y, interspersed with (Y+1) X's, plus all Z's
        # if X < Y: all of X, interspersed with (X+1) Y's, plus all Z's

        if x == y:
            return 2 * (x + y + z)
        elif x < y:
            return 2 * ((2 * x) + 1 + z)    # (x) + (x + 1) + (z)
        elif x > y:
            return 2 * ((2 * y) + 1 + z)    # (y) + (y + 1) + (z)

        # second and third cases may be combined:
        # return 2 * ((2 * min(x, y) + 1 + z))

# NOTE: Accepted on second Run (needed to multiply by string length)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.92 MB Beats 27.75%
