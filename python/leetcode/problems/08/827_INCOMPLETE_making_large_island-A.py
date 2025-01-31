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
        
        nodes = land

        # Union Find
        NodeGroup = {
            i: i
            for i in nodes
        }
        def getGroup(i: int) -> int:
            j = NodeGroup[i]
            if i != j:
                j = getGroup(j)
                NodeGroup[i] = j
            return j

        def fixGroups():
            for i in nodes:
                _ = getGroup(i)

        def sameGroup(i: int, j: int) -> bool:
            return getGroup(i) == getGroup(j)

        def mergeGroups(i: int, j: int):
            i = getGroup(i)
            j = getGroup(j)
            if i != j:
                NodeGroup[i] = j
            return

        def nodeGroupMembers() -> Dict[int,List[int]]:
            NodeGroupMembers = {}
            for i, nodeName in NodeGroup.items():
                NodeGroupMembers.setdefault(nodeName, set())
                NodeGroupMembers[nodeName].add(i)
            return NodeGroupMembers

        water_cells_adjacent = set()
        for cell in nodes:
            for neighbor in neighborsOf(cell):
                if neighbor in nodes:
                    # part of this island
                    mergeGroups(cell, neighbor)
                else:
                    # water cell next to this 
                    water_cells_adjacent.add(
                        (cell, neighbor)
                    )
        fixGroups()
        NGM = nodeGroupMembers()
        # print(f'{NGM=}')

        if len(NGM) == 1:
            return len(land) + 1

        return -99999

        island_size = {
            island_id: len(island_cells)
            for island_id, island_cells in NGM.items()
        }
        print(f'{island_size=}')

        return -99999

        # print(f'{water_cells_adjacent=}')
        islands_adjacent = {}
        for land_cell, water_cell in water_cells_adjacent:
            island_id = getGroup(land_cell)
            islands_adjacent.setdefault(water_cell, set())
            islands_adjacent[water_cell].add(island_id)
        # print(f'{islands_adjacent=}')

        return -99999

        island_groups = {
            tuple(island_id_list)
            for water_cell, island_id_list in islands_adjacent.items()
        }
        print(f'{island_groups=}')

        return -99999

        choices = [
            # [1] is for the linking cell that's turned into land
            [1] + [
                island_size[island_id]
                for island_id in island_id_list
            ]
            for water_cell, island_id_list in islands_adjacent.items()
        ]
        print(f'{choices=}')

        totals = tuple(map(sum, choices))
        print(f'{totals=}')

        return max(totals)

# NOTE: Acceptance Rate 53.6% (HARD)

# NOTE: Time Limit Exceeded
