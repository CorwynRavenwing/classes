class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        origin = (0, 0)
        target = (ROWS - 1, COLS - 1)

        def legalPos(cell: Tuple[int,int]) -> bool:
            (R, C) = cell
            return 0 <= R < ROWS and 0 <= C < COLS
        
        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)
        
        directions = [
            (X, Y)
            for X in [-1, 0, 1]
            for Y in [-1, 0, 1]
            if (X, Y) != (0, 0)
        ]
        def neighborsOf(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            nonlocal directions
            (R, C) = cell
            return [
                (R + X, C - Y)
                for (X, Y) in directions
            ]
        
        def getValue(cell: Tuple[int,int]) -> int:
            nonlocal grid
            if OOB(cell):
                return None
            (R, C) = cell
            return grid[R][C]
        
        def setValue(cell: Tuple[int,int], val: int) -> int:
            nonlocal grid
            if OOB(cell):
                return 0
            (R, C) = cell
            grid[R][C] = val
            return 1
        
        if getValue(origin) != 0:
            print(f'Origin is blocked!')
            return -1
        
        # SHORTCUT: use '2' in grid rather than a 'seen' array

        length = 0
        toCheck = {origin}
        while toCheck:
            length += 1
            print(f'{length=}')
            toCheckNext = set()
            for cell in toCheck:
                print(f'  {cell=}')
                setValue(cell, 2)
                if cell == target:
                    print(f'  SUCCESS')
                    return length
                for N in neighborsOf(cell):
                    if OOB(N):
                        # print(f'    {N=} OOB')
                        continue
                    val = getValue(N)
                    if val != 0:
                        # print(f'    {N=} {val=}')
                        continue
                    # print(f'    {N=} ok')
                    toCheckNext.add(N)
            toCheck = toCheckNext
        print(f'Ran out of paths')
        return -1

