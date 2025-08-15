class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 0:
            return False
        while n % 2 == 0:
            n //= 2
        
        return (n == 1)

# NOTE: Acceptance Rate 48.6% (easy)

# NOTE: re-ran for challenge:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.78 MB Beats 55.48%
