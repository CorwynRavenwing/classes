class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        def swap_cell_contents(P1: Tuple[int,int], P2: Tuple[int,int]) -> None:
            (x1, y1) = P1
            (x2, y2) = P2
            (
                # yes, Y is the first dimension
                matrix[y1][x1],
                matrix[y2][x2],
            ) = (
                # yes, these are backwards:
                # that is the point
                matrix[y2][x2],
                matrix[y1][x1],
            )
            return

        L = len(matrix)
        print(f'transpose diagonal')
        for Y in range(L):
            for X in range(Y, L):
                print(f'({X},{Y}) <-> ({Y},{X})')
                swap_cell_contents(
                    (X, Y),
                    (Y, X),
                )
        print(f'transpose horizontal')
        for Y in range(L):
            for X in range(L // 2):
                # don't have to swap center-line
                # on odd-sized matrices
                print(f'({X},{Y}) <-> ({L - X - 1},{Y})')
                swap_cell_contents(
                    (X, Y),
                    (L - X - 1, Y),
                )
        """
        Do not return anything, modify matrix in-place instead.
        """

