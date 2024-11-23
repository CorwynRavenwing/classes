
    def fibonacci(limit: int) -> int:
        A = 1
        yield A
        B = 1
        yield B
        while True:
            C = A + B
            if C > limit:
                return
            yield C
            (A, B) = (B, C)

