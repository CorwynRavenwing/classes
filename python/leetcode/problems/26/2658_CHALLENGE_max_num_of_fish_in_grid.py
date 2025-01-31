class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
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

        def getValues(cells: List[Tuple[int,int]]) -> List[int]:
            return [
                getValue(cell)
                for cell in cells
            ]

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

        def allCells() -> List[Tuple[int,int]]:
            return [
                (X, Y)
                for X in range(M)
                for Y in range(N)
            ]

        nodes = tuple(allCells())
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

        zeroCells = allCellsWithValue(0)
        # print(f'{zeroCells=}')
        waterCells = set(nodes) - set(zeroCells)
        # print(f'{waterCells=}')
        for water in waterCells:
            print(f'{water=}')
            for cell in neighborsOf(water):
                print(f'  {cell=}')
                if cell in zeroCells:
                    print(f'    Zero')
                    continue
                mergeGroups(water, cell)
        fixGroups()
        print(f'{NodeGroup=}')
        
        NodeGroupMembers = nodeGroupMembers()
        print(f'{NodeGroupMembers=}')

        answers = []
        for nodeName, cells in NodeGroupMembers.items():
            print(f'{nodeName=}:')
            values = getValues(cells)
            print(f'  {values=}')
            fish = sum(values)
            print(f'  -> {fish=}')
            answers.append(fish)
        print(f'{answers=}')
        return max(answers)

# NOTE: Accepted on second Run (helper function needed updating)
# NOTE: Accepted on first Submit
# NOTE: Runtime 645 ms Beats 5.12%
# NOTE: Memory 19.08 MB Beats 10.00%
