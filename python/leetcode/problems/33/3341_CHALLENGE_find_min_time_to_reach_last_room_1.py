class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        grid = moveTime     # variable rename

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

        origin = (0, 0)
        target = (M - 1, N - 1)     # they used N,M instead for some reason
        print(f'{origin} -> {target}')
        seen = set()
        queue = [(0, origin)]
        while queue:
            # print(f'Q={queue}')
            (time, cell) = queue.pop(0)
            if cell in seen:
                # print(f'{time}\t{cell}: seen')
                continue
            else:
                seen.add(cell)
            if cell == target:
                print(f'{time}\t{cell}: SUCCESS')
                return time
            # else:
            #     # print(f'DEBUG: {cell} != {target}')
            for neighbor in neighborsOf(cell):
                if neighbor in seen:
                    # print(f'{time}\t{cell}: seen {neighbor}')
                    continue
                value = getValue(neighbor)
                begin = max(time, value)
                newQ = (begin + 1, neighbor)
                # print(f'{time}\t{cell}: {newQ}')
                bisect.insort(queue, newQ)
        return -1

# NOTE: Acceptance Rate 39.9% (medium)

# NOTE: Accepted on fourth Run (they had swapped N, M variable names)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 176 ms Beats 20.16%
# NOTE: Memory 18.92 MB Beats 5.18%
