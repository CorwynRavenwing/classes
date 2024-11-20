class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        M = len(mat)
        N = len(mat[0])
        
        coords_by_diagonal = {}
        values_by_diagonal = {}
        for X in range(M):
            for Y in range(N):
                coord = (X, Y)
                value = mat[X][Y]
                diag = (X - Y)
                coords_by_diagonal.setdefault(diag, [])
                values_by_diagonal.setdefault(diag, [])
                coords_by_diagonal[diag].append(coord)
                values_by_diagonal[diag].append(value)
        
        answer = [
            [None] * N
            for X in range(M)
        ]

        for diag in values_by_diagonal.keys():
            values = values_by_diagonal[diag]
            coords = coords_by_diagonal[diag]
            values.sort()
            assert len(values) == len(coords)
            for (V, C) in zip(values, coords):
                (X, Y) = C
                answer[X][Y] = V

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 11 ms Beats 9.29%
# NOTE: Memory 17.97 MB Beats 5.50%
