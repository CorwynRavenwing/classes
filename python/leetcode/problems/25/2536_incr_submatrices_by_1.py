class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrixDeltas = [
            [0] * (n + 1)
            for rowId in range(n)
        ]
        # print(f'{matrixDeltas=}')
        for Q in queries:
            (row1i, col1i, row2i, col2i) = Q
            for rowId in range(row1i, row2i + 1):
                matrixDeltas[rowId][col1i] += 1
                matrixDeltas[rowId][col2i + 1] -= 1
            # print(f'{Q=} {matrixDeltas=}')
        
        matrix = [
            tuple(accumulate(row))[:-1]     # all but last value
            for row in matrixDeltas
        ]
        # print(f'{matrix=}')

        return matrix
# NOTE: Runtime 1567 ms Beats 63.79%
# NOTE: Memory 38.97 MB Beats 25.00%
