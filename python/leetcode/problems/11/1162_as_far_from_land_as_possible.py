class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

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

        ones = {
            (X, Y)
            for X, row in enumerate(grid)
            for Y, val in enumerate(row)
            if val == 1
        }
        print(f'{len(ones)=}')

        zeros = {
            (X, Y)
            for X, row in enumerate(grid)
            for Y, val in enumerate(row)
            if val == 0
        }
        print(f'{len(zeros)=}')

        if not ones:
            return -1
        
        if not zeros:
            return -1

        queue = ones
        distance = 0
        while queue:
            print(f'{distance=} ({len(queue)})')
            newQ = set()
            for cell in queue:
                # print(f'  {cell}:')
                for neighbor in neighborsOf(cell):
                    if getValue(neighbor) != 0:
                        # print(f'    {neighbor} skip')
                        continue
                    newQ.add(neighbor)
                    setValue(neighbor, 2)
                    # print(f'    {neighbor} OK')
            queue = newQ
            if queue:
                distance += 1
        
        # print(f'{grid=}')
        return distance

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was all-zeros edge case)
# NOTE: Runtime 425 ms Beats 5.17%
# NOTE: Memory 19.23 MB Beats 5.83%
