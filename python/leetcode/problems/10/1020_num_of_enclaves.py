class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
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

        # (1) mark all border 1's as 2's instead:
        for X in range(M):
            for Y in [0, N-1]:
                cell = (X, Y)
                if getValue(cell) == 1:
                    setValue(cell, 2)
        for Y in range(N):
            for X in [0, M-1]:
                cell = (X, Y)
                if getValue(cell) == 1:
                    setValue(cell, 2)
        
        # (2) find all 2's:
        twos = {
            (X, Y)
            for X, row in enumerate(grid)
            for Y, val in enumerate(row)
            if val == 2
        }
        print(f'{twos=}')

        # (3) cascade 2's to any adjacent 1's, making them also 2's:
        queue = twos
        while queue:
            cell = queue.pop()
            for neighbor in neighborsOf(cell):
                if getValue(neighbor) == 1:
                    setValue(neighbor, 2)
                    queue.add(neighbor)
        
        # (4) find everything that are still 1's:
        ones = {
            (X, Y)
            for X, row in enumerate(grid)
            for Y, val in enumerate(row)
            if val == 1
        }
        print(f'{ones=}')

        return len(ones)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 207 ms Beats 23.08%
# NOTE: Memory 20.67 MB Beats 83.71%
