class Solution:
    def minOperations(self, n: int) -> int:
        
        # SHORTCUT:
        # Case 1: odd count, e.g. n=7:
        # [1 3 5 7 9 11 13]
        # n // 2 = 3
        # we need to pick (5, 9) 2*1 times, (3, 11) 2*2 times, and (1, 13) 2*3 times.
        # +Triangle(3) === (3 * 4) // 2 = 6
        # the number of moves = Triangle(n // 2) * 2
        # 
        # Case 2: even count, e.g. n=8:
        # [1 3 5 7 9 11 13 15]
        # (n - 1) // 2 = 3
        # we need to pick (5, 11) 2*1 times, (3, 13) 2*2 times, and (1, 15) 2*3 times.
        # +Triangle(3) === (3 * 4) // 2 = 6
        # then we need to pick each pair once: (1, 15), (3, 13), (5, 11), (7, 9)
        # +(n // 2)
        
        def Triangle(X: int) -> int:
            return (X) * (X + 1) // 2

        if n % 2 == 0:
            # even:
            half = (n - 1) // 2
            return 2 * Triangle(half) + n // 2
        else:
            # odd:
            half = n // 2
            return 2 * Triangle(half)

# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.73 MB Beats 19.44%
