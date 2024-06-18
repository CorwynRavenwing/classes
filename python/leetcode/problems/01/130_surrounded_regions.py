class Solution:
    def solve(self, board: List[List[str]]) -> None:

        M = len(board)
        N = len(board[0])

        def neighbors_of(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            (A, B) = cell
            return [
                (A + 1, B),
                (A - 1, B),
                (A, B + 1),
                (A, B - 1),
            ]

        def legal(cell: Tuple[int,int]) -> bool:
            nonlocal M, N
            (A, B) = cell
            return (0 <= A < M) and (0 <= B < N)
        
        cells_with_O = [
            (x, y)
            for x, row in enumerate(board)
            for y, val in enumerate(row)
            if val == 'O'
        ]
        print(f'{cells_with_O=}')

        cells_to_keep = []
        for C in cells_with_O:
            print(f'O: {C}')
            for neighbor in neighbors_of(C):
                print(f'  N: {neighbor}')
                if not legal(neighbor):
                    print(f'    KEEP')
                    cells_to_keep.append(C)
                    break
                # else:
                #     print(f'    unknown')
        
        cells_to_check = cells_to_keep.copy()
        while cells_to_check:
            C = cells_to_check.pop()
            print(f'check {C}:')
            for neighbor in neighbors_of(C):
                print(f'  N: {neighbor}')
                if neighbor in cells_with_O:
                    print(f'    [O]')
                    if neighbor not in cells_to_keep:
                        print(f'      KEEP')
                        cells_to_check.append(neighbor)
                        cells_to_keep.append(neighbor)
                    else:
                        print(f'      known')
                # else:
                #     print(f'    [x] or oob')
        print(f'{cells_to_keep=}')
        cells_to_flip = [
            C
            for C in cells_with_O
            if C not in cells_to_keep
        ]
        print(f'{cells_to_flip=}')
        for (X, Y) in cells_to_flip:
            print(f'({X},{Y}): "{board[X][Y]}"', end=" ")
            board[X][Y] = 'X'
            print(f'-> "{board[X][Y]}"')

        """
        Do not return anything, modify board in-place instead.
        """

