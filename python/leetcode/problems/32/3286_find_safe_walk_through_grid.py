class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
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

        position = origin
        print(f'start: {health}')
        queue = [(health, origin)]
        seen = set()
        while queue:
            # pick the available cell with the *highest* health:
            (health, cell) = queue.pop(-1)
            health -= getValue(cell)
            if health <= 0:
                print(f'{cell}: {health} DIE')
                continue
            else:
                print(f'{cell}: {health}')
            if cell == target:
                print(f'  SUCCESS!')
                return True
            if cell in seen:
                print(f'  SEEN')
                continue
            else:
                seen.add(cell)
            for neighbor in neighborsOf(cell):
                new_record = (health, neighbor)
                # keep queue sorted:
                bisect.insort(
                    queue,
                    new_record
                )
                print(f'  +{neighbor}')
        # if we haven't found a solution yet, we fail:
        return False

# NOTE: Acceptance Rate 30.8% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case: need to sort by health)
# NOTE: Runtime 610 ms Beats 24.07%
# NOTE: Memory 18.40 MB Beats 48.14%
