class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        
        def UnionFind(nodes: List[int], edges: List[List[int]]) -> Tuple[Dict[int,List[int]],any]:
            # note: edges may be a generator
            # note: second return value is getGroup() fn
            # note: third return value is sameGroup() fn

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

            for (A, B) in edges:
                mergeGroups(A, B)

            fixGroups()
            NodeGroupMembers = nodeGroupMembers()

            return (NodeGroupMembers, getGroup, sameGroup)

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

        def allCells() -> List[Tuple[int,int]]:
            return [
                (X, Y)
                for X in range(M)
                for Y in range(N)
            ]

        nodes = allCells()
        def g_edges() -> List[List[int]]:
            for cell in nodes:
                if getValue(cell) == 0:
                    continue
                for neighbor in neighborsOf(cell):
                    if getValue(neighbor) == 0:
                        continue
                    yield (cell, neighbor)
            return
        # print(f'{nodes=}')

        edges = g_edges()
        # print(f'{tuple(g_edges())=}')
        obj = UnionFind(nodes, edges)
        (NodeGroupMembers, getGroup, sameGroup) = obj
        # print(f'{NodeGroupMembers=}')
        groups = [
            members
            for groupId, members in NodeGroupMembers.items()
            # if len(members) > 1
        ]
        # print(f'{groups=}')
        # for G in groups:
        #     print(f'{G=}')
        
        values = [
            [
                getValue(cell)
                for cell in G
            ]
            for G in groups
        ]
        print(f'{values=}')

        sums = tuple(map(sum, values))
        print(f'{sums=}')

        matches = [
            V
            for V in sums
            if V != 0
            if V % k == 0
        ]
        print(f'{matches=}')

        return len(matches)

# NOTE: Acceptance Rate 55.7% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 2263 ms Beats 5.17%
# NOTE: Memory 87.99 MB Beats 22.41%
