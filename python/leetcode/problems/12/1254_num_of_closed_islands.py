class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
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

        border_zeros = set()
        for X in [0, M-1]:
            for Y in range(N):
                cell = (X, Y)
                if getValue(cell) == 0:
                    border_zeros.add(cell)

        for X in range(M):
            for Y in [0, N-1]:
                cell = (X, Y)
                if getValue(cell) == 0:
                    border_zeros.add(cell)
        
        print(f'{border_zeros=}')
        queue = border_zeros
        while queue:
            cell = queue.pop()
            if getValue(cell) != 0:
                continue
            print(f'{cell}')
            setValue(cell, 2)
            for neighbor in neighborsOf(cell):
                if getValue(neighbor) == 0:
                    queue.add(neighbor)
                    print(f'  {neighbor}')
        
        answer = 0
        print(f'CHECKING:')
        for X in range(M):
            for Y in range(N):
                cell = (X,Y)
                value = getValue(cell)
                if value != 0:
                    continue
                answer += 1
                print(f'NEW ISLAND #{answer}')
                queue = {cell}
                while queue:
                    cell = queue.pop()
                    if getValue(cell) != 0:
                        continue
                    print(f'  {cell}')
                    setValue(cell, 2)
                    for neighbor in neighborsOf(cell):
                        if getValue(neighbor) == 0:
                            queue.add(neighbor)
                            print(f'    {neighbor}')
        
        return answer

# NOTE: Accepted on second Run (first was variable name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 89 ms Beats 5.06%
# NOTE: Memory 17.50 MB Beats 42.93%
