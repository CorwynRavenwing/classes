class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = {}
        return

    def setCell(self, cell: str, value: int) -> None:
        # we don't need to do cell-formula math,
        # so we just set and get cells by raw formula
        self.grid[cell] = value
        return

    def resetCell(self, cell: str) -> None:
        self.grid[cell] = 0
        return
    
    def getCell(self, cell: str) -> int:
        try:
            return self.grid[cell]
        except KeyError:
            return 0
    
    def getCellOrInt(self, cell: str) -> int:
        digits = '0123456789'
        if cell[0] in digits:
            return int(cell)
        else:
            return self.getCell(cell)

    def getValue(self, formula: str) -> int:
        assert formula[0] == '='
        formula = formula[1:]   # delete equal sign
        (A, B) = formula.split('+')
        return sum([
            self.getCellOrInt(A),
            self.getCellOrInt(B),
        ])

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

# NOTE: Acceptance Rate 68.1% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 72 ms Beats 89.92%
# NOTE: Memory 23.56 MB Beats 70.53%
