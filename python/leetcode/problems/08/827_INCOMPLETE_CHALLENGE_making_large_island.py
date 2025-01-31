class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        # Grid
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

        def allCellsWithValue(value: int) -> List[Tuple[int,int]]:
            return [
                (X, Y)
                for X in range(M)
                for Y in range(N)
                if getValue((X, Y)) == value
            ]

        land = allCellsWithValue(1)
        water = allCellsWithValue(0)
        # print(f'{land =}')
        # print(f'{water=}')

        if not water:
            return len(land)
        
        if not land:
            return 1
        
        for cell in land:
            setValue(cell, -1)
        
        shoreline = set()
        ISLAND_NUMBER = 0
        for cell in land:
            value = getValue(cell)
            if value != -1:
                # seen
                continue
            ISLAND_NUMBER += 1
            # print(f'{ISLAND_NUMBER=}')
            queue = {cell}
            while queue:
                cell = queue.pop()
                value = getValue(cell)
                if value == 0:
                    # print(f'  {cell}: water')
                    shoreline.add(cell)
                    continue
                if value != -1:
                    # print(f'  {cell}: seen')
                    continue
                # print(f'  {cell}: land')
                setValue(cell, ISLAND_NUMBER)
                for neighbor in neighborsOf(cell):
                    queue.add(neighbor)

        print(f'{grid=}')
        print(f'{shoreline=}')

        if ISLAND_NUMBER == 1:
            return len(land) + 1

        island_groups = set()
        for cell in shoreline:
            island_list = set()
            for neighbor in neighborsOf(cell):
                value = getValue(neighbor)
                if value == 0:
                    # water
                    continue
                if value == -1:
                    raise Exception(f'Did not clear -1 from {cell=}')
                island_list.add(value)
            island_groups.add(
                tuple(island_list)
            )
        print(f'{island_groups=}')
        
        island_size = {
            island_id: len(
                allCellsWithValue(island_id)
            )
            for island_id in range(1, ISLAND_NUMBER + 1)
        }
        print(f'{island_size=}')

        choices = [
            # [1] is for the linking cell that's turned into land
            [1] + [
                island_size[island_id]
                for island_id in island_id_list
            ]
            for island_id_list in island_groups
        ]
        print(f'{choices=}')

        totals = tuple(map(sum, choices))
        print(f'{totals=}')

        return max(totals)

# NOTE: Acceptance Rate 53.6% (HARD)

# NOTE: Time Limit Exceeded

