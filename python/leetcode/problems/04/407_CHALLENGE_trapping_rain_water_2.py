class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        grid = heightMap    # variable rename

        maxVal = max(
            map(max, grid)
        )
        print(f'{maxVal=}')
        level = [
            [maxVal for _ in row]
            for row in grid
        ]
        print(f'{level=}')
        
        M = len(grid)
        N = len(grid[0])

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

        # copy of prior which get/set Level instead of Grid:
        def getLevel(cell: Tuple[int,int]) -> int:
            (X, Y) = cell
            return level[X][Y]

        def setLevel(cell: Tuple[int,int], value: int) -> bool:
            (X, Y) = cell
            if OOB(cell):
                return False
            level[X][Y] = value
            return True

        def allCellsWithValue(value: int) -> List[Tuple[int,int]]:
            return [
                (X, Y)
                for X in range(M)
                for Y in range(N)
                if getValue((X, Y)) == value
            ]

        edgeCells = [
            (X, Y)
            for X in range(M)
            for Y in range(N)
            if (X in [0, M - 1]) or (Y in [0, N - 1])
        ]
        # print(f'{edgeCells=}')
        queue = []
        for cell in edgeCells:
            # all water flows out of each edge cell
            waterHeight = getValue(cell)
            setLevel(cell, waterHeight)
            queue.append(
                (waterHeight, cell)
            )
        queue.sort()
        # print(f'{queue=}')
        seen = set()
        while queue:
            (runOrder, cell) = queue.pop(0)
            waterHeight = getLevel(cell)
            landHeight = getValue(cell)
            print(f'L={len(queue)} H={landHeight} W={waterHeight} {cell=}')
            if cell in seen:
                print(f'  seen')
                continue
            else:
                seen.add(cell)
            neighbors = neighborsOf(cell)
            for C in neighbors:
                neighborLand = getValue(C)
                neighborWater = getLevel(C)
                print(f'  {C=} H={neighborLand} W={neighborWater}')
                if neighborWater <= neighborLand:
                    print(f'    no water')
                    continue
                if neighborWater > waterHeight:
                    neighborWater = max(waterHeight, neighborLand)
                    setLevel(C, neighborWater)
                    print(f'    -> W={neighborWater}')
                    bisect.insort(
                        queue,
                        (neighborWater, C)
                    )
                else:
                    print(f'    no change')

        print(f'{level=}')

        water = [
            [
                (waterVal - landVal)
                for landVal, waterVal in zip(landRow, waterRow)
            ]
            for landRow, waterRow in zip(heightMap, level)
        ]
        print(f'{water=}')

        return sum(
            map(sum, water)
        )

# NOTE: Acceptance Rate 48.8% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 390 ms Beats 5.21%
# NOTE: Memory 22.64 MB Beats 30.77%

# NOTE: re-ran for challenge:
# NOTE: Runtime 391 ms Beats 5.17%
# NOTE: Memory 22.53 MB Beats 26.65%
