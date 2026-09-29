class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        
        M = len(grid)
        N = len(grid[0])

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < M) and (0 <= Y < N)

        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)

        directions = (
            # (-1, 0),  # up is invalid
            (+1, 0),
            # (0, -1),  # left is invalid
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

        def allValues() -> Set[Tuple[int,int]]:
            return {
                V
                for row in grid
                for V in row
            }

        # replace parent values with "change in how many open parens"
        for cell in allCellsWithValue('('):
            setValue(cell, +1)
        for cell in allCellsWithValue(')'):
            setValue(cell, -1)
        # print(f'{grid=}')

        origin = (0, 0)
        target = (M - 1, N - 1)

        queue = {(origin, 0)}
        seen = set()
        while queue:
            # print(f'Q={len(queue)}')
            state = queue.pop()
            if state in seen:
                # print(f'{state}: SEEN')
                continue
            else:
                seen.add(state)
            (cell, total) = state
            value = getValue(cell)
            # print(f'{cell}: {total} + {value}')
            total += value
            if total < 0:
                # print(f'  FAIL: negative')
                continue
            elif cell == target:
                if total != 0:
                    # print(f'  FAIL: target but {total} != 0')
                    continue
                else:
                    # print(f'  SUCCEED!')
                    return True
            for neighbor in neighborsOf(cell):
                # print(f'  +{neighbor}: {total}')
                queue.add(
                    (neighbor, total)
                )

        return False

# NOTE: Acceptance Rate 40.9% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (Output Exceeded x2)
# NOTE: Runtime 7320 ms Beats 5.00%
# NOTE: Memory 95.49 MB Beats 31.00%
