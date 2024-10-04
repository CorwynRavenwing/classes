class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        # having noticed that each diagonal is full of cells
        # where their (X + Y) is the same for that diagonal,

        diags = {}
        for X, row in enumerate(mat):
            for Y, value in enumerate(row):
                D = X + Y
                diags.setdefault(D, [])
                diags[D].append(value)
        print(f'{diags=}')
        # This gives us each diagonal in *yellow direction* order.
        # to get *red direction* order, we reverse the even-numbered rows.

        REV = lambda x: tuple(reversed(tuple(x)))
        diagsInOrder = [
            (
                REV(diagonal)
                if rowNum % 2 == 0
                else diagonal
            )
            for rowNum, diagonal in sorted(diags.items())
        ]
        print(f'{diagsInOrder=}')

        return [
            D
            for flatten in diagsInOrder
            for D in flatten
        ]

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 171 ms Beats 10.03%
# NOTE: Memory 21.00 MB Beats 5.10%
