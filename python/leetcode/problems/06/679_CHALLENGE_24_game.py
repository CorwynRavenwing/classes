class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
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
        
        def is_24(A: Tuple[int,int]) -> bool:
            (A_num, A_den) = A
            return ((24 * A_den) == A_num)
        
        available_numbers = tuple([
            make(N, 1)
            for N in cards
        ])

        queue = [
            available_numbers
        ]

        def pattern_without_value(pattern: List[int], value: int) -> List[int]:
            assert value in pattern
            index = pattern.index(value)
            return pattern[:index] + pattern[index + 1:]

        # GENERATOR
        def all_permutations_size_K_gen(pattern: List[int], k: int) -> List[List[int]]:
            if k == 0:
                yield ()
                return

            for D in sorted(set(pattern)):
                remainder = pattern_without_value(pattern, D)
                # print(f'  {pattern=}: {D} + {remainder}')
                for value in all_permutations_size_K(remainder, k - 1):
                    yield (D,) + value
            return

        # may be cached
        def all_permutations_size_K(pattern: List[int], k: int) -> List[List[int]]:
            return tuple(all_permutations_size_K_gen(pattern, k))
        while queue:
            # print(f'\nDEBUG: Q={queue}\n')
            available_numbers = queue.pop()
            if len(available_numbers) == 1:
                (A,) = available_numbers
                if is_24(A):
                    print(f'\n\n{A} is 24!')
                    return True
                else:
                    print(f'{A} is not 24.')
                    continue

            print(f'{available_numbers=}')
            print(f'  permutations size 2:')
            for P in all_permutations_size_K(available_numbers, 2):
                (A, B) = P
                rest = available_numbers
                rest = pattern_without_value(rest, A)
                rest = pattern_without_value(rest, B)
                for op in '+-*/':
                    C = OP(op, A, B)
                    print(f'    {A} {op} {B} = {C}  {rest=}')
                    if C is None:
                        print(f'      NONE')
                        continue
                    newQ = (C,) + rest
                    queue.append(newQ)



        return False

# NOTE: Acceptance Rate 50.6% (HARD)

# NOTE: Accepted on second Run (edge case with 1/0)
# NOTE: Accepted on first Submit
# NOTE: Runtime 398 ms Beats 13.95%
# NOTE: Memory 18.44 MB Beats 7.82%
