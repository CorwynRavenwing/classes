class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        
        ACC = lambda x: (0,) + tuple(accumulate(x))
        ROWSUM = lambda G: tuple(map(ACC, G))
        INV = lambda G: tuple(zip(*G))
        COLSUM = lambda G: INV(ROWSUM(INV(G)))

        rowSums = ROWSUM(grid)
        colSums = COLSUM(grid)
        # print(f'{rowSums=}')
        # print(f'{colSums=}')

        def is_magic_square(X: int, Y: int, size: int) -> bool:
            print(f'({X},{Y}):{size}')
            # print(f'  Xsum: rowSums[{X}][{Y + size}] - rowSums[{X}][{Y}]')
            Xsum = rowSums[X][Y + size] - rowSums[X][Y]
            # print(f'  Ysum: colSums[{X + size}][{Y}] - colSums[{X}][{Y}]')
            Ysum = colSums[X + size][Y] - colSums[X][Y]
            if Xsum != Ysum:
                print(f'  NO {Xsum=} {Ysum=}')
                return False
            # print(f'  Diag: grid[{X}][{Y}]')
            Diag = grid[X][Y]
            # print(f'  revDiag: grid[{X + size - 1}][{Y}]')
            revDiag = grid[X + size - 1][Y]
            for i in range(1, size):
                # print(f'  [{i=}]')
                # print(f'  XsumI: rowSums[{X + i}][{Y + size}] - rowSums[{X + i}][{Y}]')
                XsumI = rowSums[X + i][Y + size] - rowSums[X + i][Y]
                # print(f'  YsumI: colSums[{X + size}][{Y + i}] - colSums[{X}][{Y + i}]')
                YsumI = colSums[X + size][Y + i] - colSums[X][Y + i]
                if XsumI != Xsum:
                    print(f'  NO {XsumI=} {Xsum=}')
                    return False
                if YsumI != Ysum:
                    print(f'  NO {YsumI=} {Ysum=}')
                    return False
                # print(f'  Diag: grid[{X + i}][{Y + i}]')
                Diag += grid[X + i][Y + i]
                # print(f'  revDiag: grid[{X + size - i - 1}][{Y + i}]')
                revDiag += grid[X + size - i - 1][Y + i]
            if Diag != Xsum:
                print(f'  NO {Diag=} {Xsum=}')
                return False
            if revDiag != Xsum:
                print(f'  NO {revDiag=} {Xsum=}')
                return False
            print(f'  YES {Xsum=} {Ysum=} {Diag=} {revDiag=}')
            return True

        maxSize = min(len(rowSums),len(colSums)) + 1
        largest = 1     # minimum, because every cell is a 1x1 magic square
        for X in range(len(rowSums)):
            for Y in range(len(colSums[0])):
                for size in range(largest + 1, maxSize + 1):
                    try:
                        check = grid[X + size - 1][Y + size - 1]
                    except IndexError:
                        # print(f'({X},{Y}):{size} NO out of bounds')
                        break
                        # break size -> next Y
                    if is_magic_square(X,Y,size):
                        largest = max(largest, size)

        return largest

# NOTE: Accepted on third Submit (edge case; Output Exceeded)
# NOTE: Runtime 191 ms Beats 66.23%
# NOTE: Memory 18.60 MB Beats 14.29%

# NOTE: Acceptance Rate 54.9% (medium)

# NOTE: re-ran for challenge:
# NOTE: Runtime 195 ms Beats 58.62%
# NOTE: Memory 20.18 MB Beats 6.32%
