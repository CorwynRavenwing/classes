class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
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

        fresh = {
            (X, Y)
            for X, row in enumerate(grid)
            for Y, val in enumerate(row)
            if val == 1
        }
        rotten = {
            (X, Y)
            for X, row in enumerate(grid)
            for Y, val in enumerate(row)
            if val == 2
        }
        print(f'{fresh=}')
        print(f'{rotten=}')

        queue = rotten
        answer = 0
        while queue:
            print(f'{answer=}; {queue=}')
            pass
            newQ = set()
            for cell in queue:
                for neighbor in neighborsOf(cell):
                    if neighbor in fresh:
                        newQ.add(neighbor)
            fresh -= newQ
            rotten |= newQ
            queue = newQ
            if queue:
                answer += 1

        print(f'{fresh=}')
        if fresh:
            return -1
        else:
            return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 19 ms Beats 6.69%
# NOTE: Memory 16.78 MB Beats 11.85%
