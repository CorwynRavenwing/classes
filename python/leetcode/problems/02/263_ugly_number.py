class Solution:
    def isUgly(self, n: int) -> bool:
        # print(f"{n}")
        if n == 0:
            return False
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
                # print(f"{factor} -> {n}")
        return (n == 1)

