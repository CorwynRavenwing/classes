class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        M = len(isWater)
        N = len(isWater[0])

        # grid[][] is the *height* of the cell.  isWater[][] is set up exactly backwards.
        grid = [
            [
                (
                    None    # height has not been set yet
                    if waterCell == 0
                    else 0
                )
                for waterCell in waterRow
            ]
            for waterRow in isWater
        ]

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < M) and (0 <= Y < N)

        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)

        directions = (
            (-1, 0),
            (+1, 0),
            (0, -1),
            (0, +1),
        )
        def neighborsOf(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            (X, Y) = cell
            Neighbors = (
                (X + I, Y + J)
                for (I, J) in directions
            )
            return tuple([
                C
                for C in Neighbors
                if legalPos(C)
            ])

        def getValue(cell: Tuple[int,int]) -> int:
            (X, Y) = cell
            return grid[X][Y]

        def setValue(cell: Tuple[int,int], value: int) -> bool:
            (X, Y) = cell
            if OOB(cell):
                return False
            grid[X][Y] = value
            return True

        def allCellsWithValue(value: int) -> List[Tuple[int,int]]:
            return [
                (X, Y)
                for X in range(M)
                for Y in range(N)
                if getValue((X, Y)) == value
            ]

        waterCells = allCellsWithValue(0)
        queue = set(waterCells)
        height = 0
        while queue:
            print(f'{height=} {queue=}')
            newQ = set()
            height += 1
            for Q in queue:
                for cell in neighborsOf(Q):
                    value = getValue(cell)
                    if value is not None:
                        continue
                    setValue(cell, height)
                    newQ.add(cell)
            queue = newQ
        return grid

# NOTE: Accepted on second Run (first was output-type error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 2694 ms Beats 8.41%
# NOTE: Memory 58.65 MB Beats 95.33%
