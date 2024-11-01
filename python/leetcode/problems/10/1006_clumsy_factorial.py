class Solution:
    def clumsy(self, n: int) -> int:
        
        def clumsy_recursive(n: int, subtracting=False) -> int:
            sign = (-1 if subtracting else 1)
            match n:
                case 1:
                    return (1) * sign
                case 2:
                    return (2 * 1) * sign
                case 3:
                    return (3 * 2 // 1) * sign
                case 4:
                    return (4 * 3 // 2) * sign + 1
                case _:
                    (A, B, C, D) = (n - x for x in range(1, 4+1))
                    return (n * A // B) * sign + C + clumsy_recursive(D, True)
        
        return clumsy_recursive(n)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 29 ms Beats 37.29%
# NOTE: Memory 17.34 MB Beats 21.75%
