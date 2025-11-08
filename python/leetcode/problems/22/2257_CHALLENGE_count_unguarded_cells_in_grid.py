class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        grid = [
            ['_'] * n
            for X in range(m)
        ]
        M = len(grid)
        N = len(grid[0])
        assert M == m
        assert n == n

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

        for cell in walls:
            print(f'wall : {cell}')
            setValue(cell, 'W')
        
        guardPos = set()
        for cell in guards:
            cell = tuple(cell)
            print(f'guard: {cell}')
            setValue(cell, 'G')
            guardPos.add(cell)
        
        for G in guardPos:
            for dir in directions:
                (I, J) = dir
                (X, Y) = G
                while True:
                    (X, Y) = (X + I, Y + J)
                    pos = (X, Y)
                    if OOB(pos):
                        break
                    value = getValue(pos)
                    if value in 'GW':
                        break
                    if value in '_g':
                        setValue(pos, 'g')
                        continue
                    raise Exception(f'{pos=} {value=}')
        
        unguarded = allCellsWithValue('_')
        print(f'{unguarded=}')

        return len(unguarded)

# NOTE: Acceptance Rate 65.9% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 1319 ms Beats 5.00%
# NOTE: Memory 41.88 MB Beats 65.50%

# NOTE: re-ran for challenge:
# NOTE: Runtime 1476 ms Beats 5.10%
# NOTE: Memory 42.54 MB Beats 35.71%
