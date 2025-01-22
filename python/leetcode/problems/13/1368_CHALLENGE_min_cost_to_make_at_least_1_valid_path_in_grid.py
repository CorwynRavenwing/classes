class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        M = len(grid)
        N = len(grid[0])

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < M) and (0 <= Y < N)

        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)

        directions = {
            4: (-1, 0),     # up
            3: (+1, 0),     # down
            2: (0, -1),     # left
            1: (0, +1),     # right
        }
        def neighborInDirection(cell: Tuple[int,int], dir: int) -> Tuple[int,int]:
            (X, Y) = cell
            (I, J) = directions[dir]
            return (X + I, Y + J)
        def neighborsOf(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            Neighbors = (
                neighborInDirection(cell, dir)
                for dir in directions.keys()
            )
            return tuple([
                C
                for C in Neighbors
                if legalPos(C)
            ])

        def getValue(cell: Tuple[int,int]) -> int:
            (X, Y) = cell
            return grid[X][Y]

        # def setValue(cell: Tuple[int,int], value: int) -> bool:
        #     (X, Y) = cell
        #     if OOB(cell):
        #         return False
        #     grid[X][Y] = value
        #     return True

        # def allCellsWithValue(value: int) -> List[Tuple[int,int]]:
        #     return [
        #         (X, Y)
        #         for X in range(M)
        #         for Y in range(N)
        #         if getValue((X, Y)) == value
        #     ]

        Origin = (0, 0)
        Target = (M - 1, N - 1)

        seen = set()
        queue = [
            (0, Origin)
        ]
        while queue:
            (distance, cell) = queue.pop(0)
            # print(f'L={len(queue)} D={distance} {cell}')
            if cell in seen:
                # print(f'  seen')
                continue
            else:
                seen.add(cell)
            print(f'L={len(queue)} D={distance} {cell}')
            if cell == Target:
                print(f'  FOUND')
                return distance
            sign = getValue(cell)
            signCell = neighborInDirection(cell, sign)
            if OOB(signCell):
                # print(f'  sign=OOB')
                pass
            else:
                # print(f'  sign={signCell}')
                bisect.insort(
                    queue,
                    (distance, signCell)
                )
            distance += 1
            for nextCell in neighborsOf(cell):
                if nextCell == signCell:
                    # print(f'  next=sign')
                    continue
                # print(f'  next={nextCell}')
                bisect.insort(
                    queue,
                    (distance, nextCell)
                )
        print(f'Error: ran out of Queue')
        return -1

# NOTE: Accepted on first Submit
# NOTE: Runtime 604 ms Beats 6.23%
# NOTE: Memory 23.37 MB Beats 6.23%
