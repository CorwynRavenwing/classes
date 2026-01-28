class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        
        M = len(grid)
        N = len(grid[0])

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < M) and (0 <= Y < N)

        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)

        directions = (
            # can't go Up or Left in this question:
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

        def allCellsWithLowerValue(value: int) -> List[Tuple[int,int]]:
            return [
                (X, Y)
                for X in range(M)
                for Y in range(N)
                if getValue((X, Y)) <= value
            ]

        origin = (0,0)
        target = (M-1, N-1)

        def min_not_none(L: list) -> int:
            L = list(L)
            while None in L:
                L.remove(None)
            return min(L, default=None)
        
        def sum_cascade_none(L: list) -> int:
            if None in L:
                return None
            else:
                return sum(L)
        
        # @cache
        def teleport_unconditional(value: int, k: int) -> int:
            cells = allCellsWithLowerValue(value)
            print(f'teleport({value},{k}): {cells=}')
            answers = [
                DP(location, k - 1)
                for location in cells
            ]
            retVal = min_not_none(answers)
            print(f'teleport({value},{k}) = {retVal}<-{answers}')
            return retVal

        def teleport(value: int, k: int) -> int:
            if k <= 0:
                return None
            else:
                return teleport_unconditional(value, k)

        dp_inprog = set()

        @cache
        def DP(cell, k) -> int:
            if cell in dp_inprog:
                # print(f'DP({cell},{k}): loop')
                return None
            else:
                dp_inprog.add(cell)

            print(f'DP({cell},{k})')
            if cell == target:
                print(f'DP({cell},{k}): => 0')
                dp_inprog.remove(cell)
                return 0
        
            answers = [
                (getValue(neighbor), DP(neighbor, k))
                for neighbor in neighborsOf(cell)
            ] + [
                (0, teleport(getValue(cell), k))
            ]
            print(f'DP({cell},{k}): {answers}')
            answers = tuple(map(sum_cascade_none, answers))
            print(f'DP({cell},{k}): -> {answers}')
            retVal = min_not_none(answers)
            print(f'DP({cell},{k}): => {retVal}')
            dp_inprog.remove(cell)
            return retVal

        return DP(origin, k)

# NOTE: Acceptance Rate 20.0% (HARD)

# NOTE: Wrong Answer for some inputs
