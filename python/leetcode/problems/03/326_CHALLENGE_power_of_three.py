class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n == 0:
            return False
        while n % 3 == 0:
            n //= 3

        return (n == 1)

# NOTE: Acceptance Rate 48.4% (easy)

# NOTE: re-ran for challenge
# NOTE: Runtime 7 ms Beats 73.20%
# NOTE: Memory 17.89 MB Beats 43.46%
