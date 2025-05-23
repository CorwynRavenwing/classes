class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        def dumpMatrix(label: str):
            print(f'===== {label} =====')
            for row in matrix:
                print(f'  {row}')
        
        dumpMatrix('flag:')

        (row0, col0) = (False, False)
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    if i == 0:
                        row0 = True
                        print(f'row0')
                    else:
                        matrix[i][0] = None
                        print(f'row #{i}')
                    if j == 0:
                        col0 = True
                        print(f'col0')
                    else:
                        matrix[0][j] = None
                        print(f'col #{j}')

        dumpMatrix('rows and cols:')
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] is None or matrix[0][j] is None:
                    matrix[i][j] = 0

        dumpMatrix(f'col0: {col0=}')

        for i in range(m):
            if (col0) or (matrix[i][0] is None):
                matrix[i][0] = 0

        dumpMatrix(f'row0: {row0=}')
        
        for j in range(n):
            if (row0) or (matrix[0][j] is None):
                matrix[0][j] = 0

        dumpMatrix('done')
        return

# NOTE: Runtime 107 ms Beats 31.53%
# NOTE: Memory 17.65 MB Beats 13.73%

# NOTE: re-ran for challenge:
# NOTE: Runtime 19 ms Beats 5.01%
# NOTE: Memory 19.10 MB Beats 6.55%
# NOTE: much faster, much worse percentage
# NOTE: same memory, much worse percentage
