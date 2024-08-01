class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:

        REV = lambda x: tuple(reversed(tuple(x)))

        def factorCount(value: int, factor: int) -> int:
            answer = 0
            while value % factor == 0:
                answer += 1
                value //= factor
            return answer
        
        grid25 = [
            [
                (
                    factorCount(value, 2),
                    factorCount(value, 5),
                )
                for value in row
            ]
            for row in grid
        ]
        # print(f'{grid25=}')
        
        grid2 = [
            [
                v2
                for (v2, v5) in row
            ]
            for row in grid25
        ]
        # print(f'{grid2=}')
        grid5 = [
            [
                v5
                for (v2, v5) in row
            ]
            for row in grid25
        ]
        # print(f'{grid5=}')

        def accumulate_each_row_L(grid: List[List[int]]) -> List[List[int]]:
            return [
                list(accumulate(row))
                for row in grid
            ]

        def accumulate_each_row_R(grid: List[List[int]]) -> List[List[int]]:
            return [
                REV(accumulate(REV(row)))
                for row in grid
            ]
        
        def transpose_grid(grid: List[List[int]]) -> List[List[int]]:
            return tuple(zip(*grid))

        sumRows2L = accumulate_each_row_L(grid2)
        sumRows2R = accumulate_each_row_R(grid2)
        sumRows5L = accumulate_each_row_L(grid5)
        sumRows5R = accumulate_each_row_R(grid5)
        rowSums2 = [
            row[0]
            for row in sumRows2R
        ]
        rowSums5 = [
            row[0]
            for row in sumRows5R
        ]

        transpose2 = transpose_grid(grid2)
        transpose5 = transpose_grid(grid5)

        sumCols2L = accumulate_each_row_L(transpose2)
        sumCols2R = accumulate_each_row_R(transpose2)
        sumCols5L = accumulate_each_row_L(transpose5)
        sumCols5R = accumulate_each_row_R(transpose5)

        colSums2 = [
            row[0]
            for row in sumCols2R
        ]
        colSums5 = [
            row[0]
            for row in sumCols5R
        ]

        def sum3Pair(pair1: Tuple[int,int], pair2: Tuple[int,int], pair3: Tuple[int,int]) -> Tuple[int,int]:
            # print(f'sum3Pair({pair1},{pair2},{pair3}):')
            return tuple(
                map(
                    sum,
                    zip(pair1, pair2, pair3)
                )
            )

        answers = []
        for i in range(len(grid)):
            # print(f'{i=}')
            for j in range(len(grid[0])):
                # print(f'  {j=}')
                neg_IJ = (-grid2[i][j], -grid5[i][j])
                row_L = (sumRows2L[i][j], sumRows5L[i][j])
                row_R = (sumRows2R[i][j], sumRows5R[i][j])
                col_L = (sumCols2L[j][i], sumCols5L[j][i])  # these 2 "column" grids
                col_R = (sumCols2R[j][i], sumCols5R[j][i])  # are referenced backward: J,I
                for row in [row_L, row_R]:
                    for col in [col_L, col_R]:
                        RowCol = sum3Pair(row, col, neg_IJ)
                        Min = min(RowCol)
                        if i == 3 and j == 4:
                            print(f'{i=} {j=}')
                            print(f'{row=}')
                            print(f'{col=}')
                            print(f'{neg_IJ=}')
                            print(f'  {RowCol=}')
                            print(f'    {Min=}')
                        answers.append(Min)
        print(f'{answers=}')
        return max(answers)
# NOTE: we didn't actually check for "straight" (no corner) paths
