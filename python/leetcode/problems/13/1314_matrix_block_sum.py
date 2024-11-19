class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        M = len(mat)
        N = len(mat[0])

        gridPartialSums = tuple(
            (0,) + tuple(accumulate(row))
            for row in mat
        )
        
        answer = [
            [
                [
                    gridPartialSums[r][c2 + 1] - gridPartialSums[r][c1]
                    for r in range(i - k, i + k + 1)
                    for c1 in [max(0, j - k)]
                    for c2 in [min(N - 1, j + k)]
                    if 0 <= r < M
                ]
                for j in range(N)
            ]
            for i in range(M)
        ]
        print(f'{answer=}')
        answer = [
            [
                sum(values)
                for values in row
            ]
            for row in answer
        ]
        return answer

# NOTE: Accepted on second Run (variable-name typo)
# NOTE: Accepted on third Submit (output exceeded; time exceeded)
# NOTE: Runtime 719 ms Beats 14.46%
# NOTE: Memory 57.48 MB Beats 5.18%
