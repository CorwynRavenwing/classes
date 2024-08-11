class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        # we borrow some code from #2556, even though that didn't work

        grid_R = len(grid)
        grid_C = len(grid[0])
        
        directions = (
            (-1, 0),
            (+1, 0),
            (0, -1),
            (0, +1),
        )
        
        activeCells = {
            (R, C)
            for R, row in enumerate(grid)
            for C, value in enumerate(row)
            if value == 1
        }

        @cache
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
        
        # pick any random "active" point
        if len(activeCells) == 0:
            print(f'Yes: already zero islands')
            return 0

        origin = tuple(activeCells)[0]
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

        # cells_with_LE_2_adjacent = [
        #     cell
        #     for cell, neighbors in adjacent.items()
        #     if len(neighbors) <= 2
        # ]
        # print(f'cells_with_LE_2_adjacent=')

        # cells_with_3_adjacent = [
        #     cell
        #     for cell, neighbors in adjacent.items()
        #     if len(neighbors) == 3
        # ]
        # print(f'cells_with_3_adjacent=')
        
        def countRegionsAvoiding(avoidCell=None) -> int:
            # print(f'countRegionsAvoiding({avoidCell}):')
            # here we borrow some code from #959:
            seen = set()
            regions = 0
            for cell in activeCells:
                if cell in seen:
                    continue
                else:
                    seen.add(cell)
                # print(f'{cell}')
                if (avoidCell is not None) and (cell == avoidCell):
                    # print(f'  (AVOID)')
                    continue
                regions += 1
                # print(f'NEW REGION #{regions}')
                queue = {cell}
                # paint out this region:
                while queue:
                    Q = queue.pop()
                    # print(f'  {regions}: {Q}')
                    for N in neighborsOf(Q):
                        if N in seen:
                            continue
                        else:
                            seen.add(N)
                        # print(f'    {N=}')
                        if (avoidCell is not None) and (N == avoidCell):
                            # print(f'      (AVOID)')
                            continue
                        # MUST BE AFTER AVOIDCELL SECTION
                        queue.add(N)
            return regions

        regions = countRegionsAvoiding()
        if regions > 1:
            print(f'ALREADY >1 ISLAND: {regions=}')
            return 0
        
        # print(f'CHECKING {cells_with_LE_2_adjacent=}')
        # for avoidCell in cells_with_LE_2_adjacent:
        #     print(f'Try {avoidCell=}')
        #     regions = countRegionsAvoiding(avoidCell)
        #     if regions != 1:
        #         print(f'  YES: {regions=}')
        #         return 1
        
        # print(f'CHECKING {cells_with_3_adjacent=}')
        # for avoidCell in cells_with_3_adjacent:
        #     print(f'Try {avoidCell=}')
        #     regions = countRegionsAvoiding(avoidCell)
        #     if regions != 1:
        #         print(f'  YES: {regions=}')
        #         return 1
        
        # print(f'CHECKING {activeCells=}')
        for avoidCell in activeCells:
            print(f'Try {avoidCell=}')
            regions = countRegionsAvoiding(avoidCell)
            if regions != 1:
                print(f'  YES: {regions=}')
                return 1

        # otherwise, we can just carve off a corner somewhere in 2 moves
        return 2
# NOTE: Runtime 691 ms Beats 61.68%
# NOTE: Memory 17.46 MB Beats 15.89%
