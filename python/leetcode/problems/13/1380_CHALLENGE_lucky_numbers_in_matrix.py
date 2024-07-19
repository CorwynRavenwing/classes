class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        row_minima = set(
            map(
                min,
                matrix,
            )
        )
        print(f'{row_minima=}')
        column_maxima = set(
            map(
                max,
                zip(*matrix),   # transpose row/col
            )
        )
        print(f'{column_maxima=}')
        return row_minima & column_maxima   # "&" == intersection
# NOTE: Runtime 109 ms; Beats 64.66%
# NOTE: O(M * N)
# NOTE: Memory 16.78 MB; Beats 79.04%
# NOTE: O(M + N)
