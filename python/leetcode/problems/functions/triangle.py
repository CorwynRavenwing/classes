        def Triangle(N: int) -> int:
            return (N) * (N + 1) // 2

        def ReverseTriangle(S: int) -> int:
            # number whose triangle function "N*(N + 1)/2" is S:
            return int(math.sqrt(2 * S))

