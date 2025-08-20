        
        # we're writing functions to handle fractions:
        # all numbers are a Tuple[int,int]: (numerator, denominator)

        def make(numerator: int, denominator: int) -> Tuple[int,int]:
            if denominator < 0:
                return make(-numerator, -denominator)
            elif denominator == 0:
                return None
            else:
                return (numerator, denominator)

        def neg(A: Tuple[int,int]) -> Tuple[int,int]:
            if A is None:
                return None
            (numerator, denominator) = A
            return make(-numerator, denominator)

        def add(A: Tuple[int,int], B: Tuple[int,int]) -> Tuple[int,int]:
            if A is None or B is None:
                return None
            (A_num, A_den) = A
            (B_num, B_den) = B
            return make(
                A_num * B_den + B_num * A_den,
                A_den * B_den
            )

        def sub(A: Tuple[int,int], B: Tuple[int,int]) -> Tuple[int,int]:
            if A is None or B is None:
                return None
            return add(neg(A), B)

        def inv(A: Tuple[int,int]) -> Tuple[int,int]:
            if A is None:
                return None
            (numerator, denominator) = A
            if numerator == 0:
                return None
            return make(denominator, numerator)

        def mul(A: Tuple[int,int], B: Tuple[int,int]) -> Tuple[int,int]:
            if A is None or B is None:
                return None
            (A_num, A_den) = A
            (B_num, B_den) = B
            return make(
                A_num * B_num,
                A_den * B_den
            )

        def div(A: Tuple[int,int], B: Tuple[int,int]) -> Tuple[int,int]:
            if A is None or B is None:
                return None
            return mul(A, inv(B))
        
        def OP(op: str, A: Tuple[int,int], B: Tuple[int,int]) -> Tuple[int,int]:
            match op:
                case '+':
                    return add(A,B)
                case '-':
                    return sub(A,B)
                case '*':
                    return mul(A,B)
                case '/':
                    return div(A,B)
                case _:
                    raise Exception(f'OP() called with invalid {op=}: should be + - * /')
        
