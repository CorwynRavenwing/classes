class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle
        return

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rect[row][col] = newValue
        return

    def getValue(self, row: int, col: int) -> int:
        return self.rect[row][col]

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 137 ms Beats 64.54%
# NOTE: Memory 18.73 MB Beats 25.68%
