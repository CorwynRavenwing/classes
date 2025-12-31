class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        # UNION FIND:

        def UnionFind(nodes: List[int], edges: List[List[int]]) -> Tuple[Dict[int,List[int]],any,any]:
            # print(f'\nUnionFind():')
            # note: edges may be a generator
            # note: second return value is getGroup() fn
            # note: third return value is sameGroup() fn
            NodeGroup = {
                i: i
                for i in nodes
            }
            # print(f'DEBUG: {NodeGroup=}')
            def getGroup(i: int) -> int:
                # print(f'DEBUG: getGroup({i})')
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

            def nodeGroupMembers() -> Tuple[Dict[int,List[int]],any]:
                NodeGroupMembers = {}
                for i, nodeName in NodeGroup.items():
                    NodeGroupMembers.setdefault(nodeName, set())
                    NodeGroupMembers[nodeName].add(i)
                return NodeGroupMembers

            for (A, B) in edges:
                mergeGroups(A, B)

            fixGroups()
            return (nodeGroupMembers(), getGroup, sameGroup)

        # GRID FUNCTIONS:

        grid = None     # will be set later

        M = row     # len(grid)
        N = col     # len(grid[0])

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < M) and (0 <= Y < N)

        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)

        # we ony need Down and Right, as we are using Union Find to connect nodes
        directions = (
            # (-1, 0),
            (+1, 0),
            # (0, -1),
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
            # print(f'DEBUG: getValue({cell})')
            (X, Y) = cell
            return grid[X][Y]

        def setValue(cell: Tuple[int,int], value: int) -> bool:
            (X, Y) = cell
            if OOB(cell):
                return False
            grid[X][Y] = value
            return True

        def allCellsWithValue(value: int) -> List[Tuple[int,int]]:
            # print(f'DEBUG: allCellsWithValue({value})')
            # print(f'DEBUG: allCellsWithValue(): X in {tuple(range(M))}')
            # print(f'DEBUG: allCellsWithValue(): Y in {tuple(range(N))}')
            answer = [
                (X, Y)
                for X in range(M)
                for Y in range(N)
                if getValue((X, Y)) == value
            ]
            # print(f'DEBUG: allCellsWithValue({value}): {len(answer)}')
            return answer

        grid = [
            [0] * col
            for _ in range(row)
        ]

        def isPossible() -> bool:
            # can cross with current grid?
            nodes = set(allCellsWithValue(0))
            # print(f'DEBUG: {nodes       =}')
            TOP = 'top'
            BOTTOM = 'bottom'
            nodes.add(TOP)
            nodes.add(BOTTOM)
            top_nodes = top_row & nodes
            bottom_nodes = bottom_row & nodes
            # print(f'DEBUG: {top_nodes   =}')
            # print(f'DEBUG: {bottom_nodes=}')

            def edges_gen() -> List[Tuple[int,int]]:
                for Node in nodes:
                    neighbors = (
                        top_nodes if Node == TOP else
                        bottom_nodes if Node == BOTTOM else
                        neighborsOf(Node)
                    )
                    # print(f'DEBUG: edges {Node} -> {neighbors}')
                    for Neighbor in neighbors:
                        if getValue(Neighbor) == 0:
                            yield[Node, Neighbor]
                        # skip neighbors that are water cells
                return
            
            (nodeGroupMembers, getGroup, sameGroup) = UnionFind(nodes, edges_gen())
            # print(f'NGM={nodeGroupMembers}')
            # print(f'{target=} {getGroup(TOP)=} {getGroup(BOTTOM)=} {sameGroup(TOP,BOTTOM)=}')

            answer = sameGroup(TOP,BOTTOM)
            # print(f'isPossible({target}): END {answer=}')
            return answer
        
        top_row = {
            (0, Y)
            for Y in range(col)
        }
        bottom_row = {
            (row - 1, Y)
            for Y in range(col)
        }

        prior_answer = True     # before any Cells, you can always cross
        answer = False          # we don't know this answer yet
        prior_t = 0
        t = 0

        for cell1 in cells:
            prior_t = t
            prior_answer = answer
            t += 1
            (Xi, Yi) = cell1
            (X, Y) = ((Xi - 1), (Yi - 1))   # grid is 0-based; coords are 1-based
            cell0 = (X, Y)
            setValue(cell0, 1)      # fill cell with water

            answer = isPossible()
            if prior_answer and not answer:
                return prior_t
        
        return t

# NOTE: Acceptance Rate 63.4% (HARD)

# NOTE: linear search also gives TLE
