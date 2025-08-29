class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        X_size = len(grid)
        Y_size = len(grid[0])

        # @cache
        def matrix_to_diagonal_coords() -> List[List[Tuple[int,int]]]:
            # nonlocal X_size, Y_size
            grid_coords = [
                [
                    (X, Y)
                    for Y in range(Y_size)
                ]
                for X in range(X_size)
            ]

            answer = []
            working = []
            # print(f'{grid_coords=} {working=} {answer=}')
            row = grid_coords.pop(0)
            while row:
                working.append(
                    [
                        row.pop(-1)
                    ]
                )
            # print(f'{grid_coords=} {working=} {answer=}')
            while grid_coords:
                answer.append(
                    working.pop(0)
                )
                working.append([])
                row = grid_coords.pop(0)
                assert len(working) == len(row)
                for W_ref in working:
                    W_ref.append(
                        row.pop(-1)
                    )
                # print(f'{grid_coords=} {working=} {answer=}')
            while working:
                answer.append(
                    working.pop(0)
                )
                # print(f'{grid_coords=} {working=} {answer=}')
            # print(f'{answer=}')
            return tuple(map(tuple, answer))

        def matrix_to_diagonals(grid: List[List[int]]) -> List[List[int]]:
            # nonlocal X_size, Y_size
            coords = matrix_to_diagonal_coords()
            # print(f'{coords=}')
            diagonals = [
                [
                    grid[X][Y]
                    for (X,Y) in coords_row
                ]
                for coords_row in coords
            ]
            # print(f'{diagonals=}')
            return diagonals
        
        diagonals = matrix_to_diagonals(grid)
        print(f'raw {diagonals=}')

        def silly_sort_diagonals(diagonals: List[List[int]]) -> List[List[int]]:
            index = (len(diagonals) - 1) // 2
            # print(f'{index=}')
            top_half = diagonals[:index]
            bottom_half = diagonals[index:]
            # print(f'raw {top_half=}')
            # print(f'raw {bottom_half=}')
            SORT_ASC = lambda L: tuple(sorted(L))
            SORT_DESC = lambda L: tuple(sorted(L, reverse=True))
            top_half = tuple(map(SORT_ASC, top_half))
            bottom_half = tuple(map(SORT_DESC, bottom_half))
            # print(f'sorted {top_half=}')
            # print(f'sorted {bottom_half=}')
            return top_half + bottom_half

        diagonals = silly_sort_diagonals(diagonals)
        print(f'sorted {diagonals=}')

        def diagonals_to_matrix(diagonals: List[List[int]]) -> List[List[int]]:
            # nonlocal X_size, Y_size
            coords = matrix_to_diagonal_coords()
            # print(f'{coords=}')
            answer = [
                [None] * Y_size
                for X in range(X_size)
            ]
            for diag_row, coords_row in enumerate(coords):
                for diag_column, (X,Y) in enumerate(coords_row):
                    answer[X][Y] = diagonals[diag_row][diag_column]
            # print(f'{answer=}')
            return answer
        
        answer = diagonals_to_matrix(diagonals)
        # print(f'{answer=}')

        return answer

# NOTE: Acceptance Rate 72.2% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 47 ms Beats 5.42%
# NOTE: Memory 18.52 MB Beats 9.17%
