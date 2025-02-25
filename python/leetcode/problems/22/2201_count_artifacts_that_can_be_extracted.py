class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:

        grid = [
            [0] * n
            for _ in range(n)
        ]

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

        # def allCellsWithValue(value: int) -> List[Tuple[int,int]]:
        #     return [
        #         (X, Y)
        #         for X in range(M)
        #         for Y in range(N)
        #         if getValue((X, Y)) == value
        #     ]

        for cell in dig:
            setValue(cell, 1)
        # print(f'{grid=}')

        answer = 0
        for index, (r1, c1, r2, c2) in enumerate(artifacts):
            found = True
            for X in range(r1, r2 + 1):
                for Y in range(c1, c2 + 1):
                    print(f'[{index}]: ({X},{Y})')
                    cell = (X, Y)
                    value = getValue(cell)
                    if value == 0:
                        print(f'  NO')
                        found = False
                        break
                if not found:
                    break
            if found:
                print(f'  YES')
                answer += 1

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 262 ms Beats 8.33%
# NOTE: Memory 61.06 MB Beats 85.42%
