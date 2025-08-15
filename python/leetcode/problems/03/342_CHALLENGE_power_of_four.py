class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n == 0:
            return False
        while n % 4 == 0:
            n //= 4

        return (n == 1)

# NOTE: Acceptance Rate 49.8% (easy)

# NOTE: re-ran for challenge:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.88 MB Beats 38.66%
