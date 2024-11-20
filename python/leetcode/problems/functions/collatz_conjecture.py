
        @cache
        def Collatz(x: int) -> int:
            if x == 1:
                return 0
            if x % 2 == 0:
                new_x = x // 2
            else:
                new_x = 3 * x + 1
            return 1 + Collatz(new_x)

