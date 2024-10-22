class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
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

        WATER = 0
        LAND = 1
        SHORE = 2
        INTERIOR = 3
        BRIDGE = 9

        # 0. Find any "1" cell.
        for X, row in enumerate(grid):
            for Y, val in enumerate(row):
                if val == LAND:
                    firstCell = (X, Y)
                    break
        
        # 1. depth-first search for the rest of this island,
        # especially the shoreline.

        island = {firstCell}
        shore = set()
        while island:
            print(f'Island={len(island)} Shore={len(shore)}')
            cell = island.pop()
            adjacent_cells = neighborsOf(cell)
            adjacent_values = tuple(map(getValue, adjacent_cells))
            if WATER in adjacent_values:
                setValue(cell, SHORE)
                shore.add(cell)
            else:
                setValue(cell, INTERIOR)
            for (neighbor, value) in zip(adjacent_cells, adjacent_values):
                if value == LAND:
                    island.add(neighbor)
        
        # 2. breadth-first search for the other island, counting bridge length.

        distance = 0
        bridge = shore
        while bridge:
            new_bridge = set()
            for cell in bridge:
                setValue(cell, BRIDGE)
                for neighbor in neighborsOf(cell):
                    value = getValue(neighbor)
                    if value == LAND:
                        return distance
                    elif value == WATER:
                        new_bridge.add(neighbor)
            bridge = new_bridge
            distance += 1
        
        # 3. give up because we shouldn't get here

        raise Exception(f'We did not find an answer')

# NOTE: Accepted on first Submit
# NOTE: Runtime 145 ms Beats 93.92%
# NOTE: Memory 17.72 MB Beats 80.34%
