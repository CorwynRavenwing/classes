class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        positionByValue = [None] * (len(arr) + 1)
        for X, row in enumerate(mat):
            for Y, val in enumerate(row):
                assert positionByValue[val] is None
                positionByValue[val] = (X, Y)
        print(f'{positionByValue=}')

        M = len(mat)
        N = len(mat[0])

        # here we are counting unpainted cells:
        rows = [N] * M
        cols = [M] * N

        for i, val in enumerate(arr):
            cell = positionByValue[val]
            print(f'[{i}]={val} @{cell}')
            (X, Y) = cell
            rows[X] -= 1
            cols[Y] -= 1
            print(f'  R={rows[X]} C={cols[Y]}')
            if rows[X] == 0 or cols[Y] == 0:
                return i

        return -99999

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 515 ms Beats 5.36%
# NOTE: Memory 44.80 MB Beats 95.58%
