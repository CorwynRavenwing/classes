class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        INV = lambda L: tuple(zip(*L))
        SUM = lambda L: tuple(map(sum, L))

        invmat = INV(mat)
        x_sums = SUM(mat)
        y_sums = SUM(invmat)

        # print(f'{invmat=}')
        # print(f'{x_sums=}')
        # print(f'{y_sums=}')

        answers = [
            ((X, Y), x_sums[X], y_sums[Y])
            for X in range(len(mat))
            for Y in range(len(mat[0]))
            if mat[X][Y] == 1
            if x_sums[X] == 1
            if y_sums[Y] == 1
        ]
        # print(f'{answers=}')

        return len(answers)

# NOTE: Acceptance Rate 69.3% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 1 ms Beats 91.91%
# NOTE: Memory 19.50 MB Beats 93.85%
