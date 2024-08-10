class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        
        # testcase:
        # [[1,1,1,1,1,0],[1,1,1,1,0,0],[0,0,0,0,0,0],[0,1,1,1,1,1],[1,1,1,1,1,1],[0,0,0,0,1,1]]
        grid_R = len(grid)
        grid_C = len(grid[0])

        origin = (0,0)
        target = (grid_R - 1, grid_C - 1)

        directions = (
            (+1, 0),
            (-1, 0),
            (0, +1),
            (0, -1),
        )

        activeCells = {
            (R, C)
            for R, row in enumerate(grid)
            for C, value in enumerate(row)
            if value == 1
        }
        # print(f'{activeCells=}')

        # # we may not need these three functions this time
        # def legalPos(cell: Tuple[int,int]) -> bool:
        #     (R, C) = cell
        #     return (0 <= R < grid_R) and (0 <= C < grid_C)

        # def OOB(cell: Tuple[int,int]) -> bool:
        #     return not legalPos(cell)

        # def valueAT(cell: Tuple[int,int]) -> int:
        #     (R, C) = cell
        #     return grid[R][C]   # assuming not OOB here
        
        def neighborsOf(cell):
            (R, C) = cell
            possibleNeighbors = [
                (R + I, C + J)
                for (I, J) in directions
            ]
            return [
                N
                for N in possibleNeighbors
                if N in activeCells
                # if this runs out of memory, instead check legalPos and valueAt == 1
            ]
        
        adjacent = {}
        queue = {origin}
        while queue:
            pos = queue.pop()
            # print(f'{pos=}')
            if pos in adjacent:
                # print(f'  (seen)')
                continue
            adjacent.setdefault(pos, set())
            for N in neighborsOf(pos):
                # print(f'  {N=}')
                adjacent[pos].add(N)
                queue.add(N)
        # print(f'{adjacent=}')
        if target not in adjacent:
            print(f'WE NEVER REACHED THE TARGET CELL!')
            print(f'  Already disconnected.')
            return True
        
        def isConnectedWhileAvoiding(avoidCell: Tuple[int,int]) -> bool:
            queue = {origin}
            seen = set()
            while queue:
                print(f'L={len(queue)}')
                if target in queue:
                    print(f'  TARGET {target} REACHABLE')
                    return True
                newQ = set()
                for pos in queue:
                    # print(f'  {pos=}')
                    if pos in seen:
                        # print(f'  (seen)')
                        continue
                    else:
                        seen.add(pos)
                    if pos == avoidCell:
                        # print(f'  Skip {avoidCell}')
                        continue
                    for N in adjacent[pos]:
                        # print(f'    {N=}')
                        newQ.add(N)
                queue = newQ
            print(f'  No connection found')
            return False

        for avoidCell in activeCells:
            print(f'Avoiding {avoidCell}:')
            if avoidCell in [origin, target]:
                print(f'  Skip origin/target')
                continue
            if isConnectedWhileAvoiding(avoidCell):
                print(f'  Still connected')
                continue
            return True
# NOTE: works, but times out for huge input.
