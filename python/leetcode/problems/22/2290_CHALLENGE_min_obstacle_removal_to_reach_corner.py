class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
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

        origin = (0, 0)
        target = (M - 1, N - 1)

        seen = set()
        queue = [(0, origin)]
        while queue:
            (distance, cell) = queue.pop(0)
            # print(f'{distance}: {cell}:')
            if cell in seen:
                # print(f'  (seen)')
                continue
            else:
                seen.add(cell)
            
            if cell == target:
                # print(f'  FOUND!')
                return distance
            
            for neighbor in neighborsOf(cell):
                if neighbor in seen:
                    continue
                value = getValue(neighbor)
                # print(f'  -> {neighbor} ({value})')
                bisect.insort(
                    queue,
                    (distance + value, neighbor)
                )

        raise Exception(f'Error: never reached the target cell')

# NOTE: Acceptance Rate 58.7% (HARD)
# NOTE: Runtime 5130 ms Beats 5.22%
# NOTE: Memory 48.45 MB Beats 24.10%
