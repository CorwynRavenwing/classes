class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:

        # per hint #2
        A = tuple([
            ((x, y), value - 1)     # === count of extra stones
            for x, row in enumerate(grid)
            for y, value in enumerate(row)
            if value > 1
        ])
        B = tuple([
            (x, y)
            for x, row in enumerate(grid)
            for y, value in enumerate(row)
            if value == 0
        ])
        print(f'{A=}')
        print(f'{B=}')

        # @cache
        def distance(cell1: Tuple[int,int], cell2: Tuple[int,int]) -> int:
            (X1, Y1) = cell1
            (X2, Y2) = cell2
            return sum([
                abs(X1 - X2),
                abs(Y1 - Y2),
            ])

        @cache
        def moves(A: Tuple[Tuple[int,int],int], B: Tuple[int,int]) -> int:
            print(f'moves({A},{B})')
            if not A and not B:
                return 0
            
            if not A or not B:
                raise Exception(f'Error: {A=} and {B=} should either both be empty or neither')
            
            B_pick = B[0]
            B_others = B[1:]
            print(f'Chose {B_pick=}')
            
            answers = []
            for i, A_pick in enumerate(A):
                (A_cell, A_count) = A_pick
                A_decrement = (
                    tuple([(A_cell, A_count - 1)])
                    if A_count > 1
                    else ()
                )
                A_others = A[:i] + A_decrement + A[i + 1:]
                answers.append(
                    sum([
                        distance(B_pick, A_cell),
                        moves(A_others, B_others),
                    ])
                )
            return min(answers)
        
        return moves(A, B)
# NOTE: Runtime 79 ms Beats 63.09%
# NOTE: Memory 16.98 MB Beats 19.52%
