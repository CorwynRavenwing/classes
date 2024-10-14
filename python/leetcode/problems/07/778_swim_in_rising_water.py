class Solution:
    def networkDelay(self, adjacent: Dict[any,Dict[any,int]], source: any, target: any) -> int:
        nodeDelay = {}
        queue = [(0, source)]    # second 0, node "source"
        while queue:
            (time, node) = queue.pop(0)     # earliest time
            # print(f'{node=} {time=}')
            if node in nodeDelay:
                # print(f'  (seen)')
                continue
            else:
                nodeDelay[node] = time
                if node not in adjacent:
                    # print(f'  (no neighbors)')
                    continue
                neighbors = adjacent[node]
                for (nextNode, delay) in neighbors.items():
                    newTime = time + delay
                    bisect.insort(
                        queue,
                        (newTime, nextNode)
                    )
        try:
            answer = nodeDelay[target]
        except KeyError:
            answer = None
        return answer

    def swimInWater(self, grid: List[List[int]]) -> int:
        
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

        origin = (0,0)
        target = (M-1, N-1)

        coordinatesByValue = {}
        for X, row in enumerate(grid):
            for Y, value in enumerate(row):
                coordinatesByValue.setdefault(value, set())
                coordinatesByValue[value].add(
                    (X,Y)
                )
        print(f'{coordinatesByValue=}')

        adjacent = {}
        for depth in sorted(coordinatesByValue.keys()):
            print(f'{depth=}')
            for coord in coordinatesByValue[depth]:
                print(f'  {coord}:')
                for neighbor in neighborsOf(coord):
                    value = getValue(neighbor)
                    if value > depth:
                        print(f'    nope ({value})')
                        continue
                    print(f'    yes ({value})')
                    adjacent.setdefault(coord, {})
                    adjacent[coord][neighbor] = 1
                    adjacent.setdefault(neighbor, {})
                    adjacent[neighbor][coord] = 1
            delay = self.networkDelay(adjacent, origin, target)
            print(f'  {delay=}')
            if delay is not None:
                return depth

        return None

# NOTE: Acceptance Rate 61.6% (HARD)
# NOTE: Accepted on first Submit
# NOTE: Runtime 3880 ms Beats 5.19%
# NOTE: Memory 18.90 MB Beats 5.35%
