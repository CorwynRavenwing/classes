class NumMatrix:

    # we borrow some code from #303:

    def __init__(self, matrix: List[List[int]]):
        SUM = lambda x: tuple(accumulate(x))
        INV = lambda x: tuple(zip(*tuple(x)))

        print(f'input matrix:')
        for row in matrix:
            print(f'  {row}')

        partialSumsX = [SUM(row) for row in matrix]
        print(f'partialSumsX:')
        for row in partialSumsX:
            print(f'  {row}')

        partialSumsY = INV([
            SUM(row)
            for row in INV(partialSumsX)
        ])
        print(f'partialSumsY:')
        for row in partialSumsY:
            print(f'  {row}')

        self.partialSums = partialSumsY
        # throw away matrix itself
        # print(f'self.partialSums:')
        # for row in self.partialNums:
        #     print(f'  {row}')

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        print(f'sumRegion({row1},{col1})({row2},{col2})')
        ABCD = self.partialSums[row2][col2]
        BD = self.partialSums[row2][col1 - 1] if col1 else 0
        CD = self.partialSums[row1 - 1][col2] if row1 else 0
        D = self.partialSums[row1 - 1][col1 - 1] if (row1 and col1) else 0
        A = ABCD - BD - CD + D
        print(f'  +{ABCD=} -{BD=} -{CD=} +{D=} -> {A=}')
        return A

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# NOTE: Accepted on first Submit
# NOTE: Runtime 1162 ms Beats 13.47%
# NOTE: Memory 29.42 MB Beats 5.73%
