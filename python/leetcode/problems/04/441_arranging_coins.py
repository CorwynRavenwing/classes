class Solution:
    def arrangeCoins(self, n: int) -> int:

        rows = 0
        rowSize = 1
        print(f"{rows=} {rowSize=} {n=}")
        while n >= rowSize:
            rows += 1
            n -= rowSize
            rowSize += 1
            print(f"{rows=} {rowSize=} {n=}")
        return rows

