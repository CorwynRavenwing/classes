class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:

        def legalCell(cell: Tuple[int,int]) -> bool:
            # nonlocal grid
            (X, Y) = cell
            return 0 <= X < len(grid) and 0 <= Y < len(grid[0])
        
        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalCell(cell)
        
        def getColor(cell: Tuple[int,int]) -> int:
            if OOB(cell):
                return None
            (X, Y) = cell
            return grid[X][Y]

        def setColor(cell: Tuple[int,int], newColor: int) -> bool:
            nonlocal grid
            if OOB(cell):
                return False
            (X, Y) = cell
            grid[X][Y] = newColor
            return True
        
        def setColors(cells: Set[Tuple[int,int]], newColor: int) -> int:
            ok = 0
            for cell in cells:
                if setColor(cell, newColor):
                    ok += 1
            return ok

        def neighborsOf(cell: Tuple[int,int]) -> Set[Tuple[int,int]]:
            (X, Y) = cell
            return {
                (X - 1, Y),
                (X + 1, Y),
                (X, Y - 1),
                (X, Y + 1),
            }
        
        origin = (row, col)
        toCheck = {origin}
        connected = {origin}
        border = set()
        originColor = getColor(origin)
        while toCheck:
            toCheckNext = set()
            for cell in toCheck:
                print(f'check {cell=}')
                isBorder = False
                for N in neighborsOf(cell):
                    print(f'  {N=}')
                    if N in connected:
                        print(f'    already connected')
                        continue
                    if OOB(N):
                        print(f'    OOB')
                        isBorder = True
                        continue
                    neighborColor = getColor(N)
                    if neighborColor != originColor:
                        print(f'    Color {neighborColor}')
                        isBorder = True
                        continue
                    print(f'    OK')
                    toCheckNext.add(N)
                    connected.add(N)
                if isBorder:
                    print(f'  -> border')
                    border.add(cell)
                else:
                    print(f'  -> interior')
            toCheck = toCheckNext
        print(f'{connected=}')
        print(f'{border=}')
        print(f'interior={connected - border}')

        X = setColors(border, color)
        print(f'set colors of {X} border cells to {color}')
        return grid

