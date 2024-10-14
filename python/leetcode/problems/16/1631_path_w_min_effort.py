class Solution:

    # we borrow some code from #778:

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
                    # use MAX instead of SUM here:
                    newTime = max(time, delay)
                    bisect.insort(
                        queue,
                        (newTime, nextNode)
                    )
        try:
            answer = nodeDelay[target]
        except KeyError:
            answer = None
        return answer

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        grid = heights  # variable rename

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

        adjacent = {}
        for X, row in enumerate(grid):
            for Y, value in enumerate(row):
                coord = (X, Y)
                value1 = getValue(coord)
                for neighbor in neighborsOf(coord):
                    value2 = getValue(neighbor)
                    effort = abs(value1 - value2)
                    adjacent.setdefault(coord, {})
                    adjacent[coord][neighbor] = effort
                    adjacent.setdefault(neighbor, {})
                    adjacent[neighbor][coord] = effort

        delay = self.networkDelay(adjacent, origin, target)
        print(f'  {delay=}')
        return delay

# NOTE: Accepted on first Submit
# NOTE: Runtime 1767 ms Beats 10.90%
# NOTE: Memory 23.65 MB Beats 5.18%
