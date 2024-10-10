class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
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

        islandNumber = 0
        Islands = {}
        answers = []
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                print(f'({x},{y}): {val}')
                if not val:
                    continue
                pos = (x,y)
                if pos in Islands:
                    print(f'  (seen)')
                    continue
                islandNumber += 1
                print(f'  NEW ISLAND #{islandNumber}')
                queue = {pos}
                size = 0
                while queue:
                    Q = queue.pop()
                    print(f'    {Q}:')
                    if Q in Islands:
                        print(f'      (seen)')
                        continue
                    else:
                        Islands[Q] = islandNumber
                        size += 1
                    for R in neighborsOf(Q):
                        (X, Y) = R
                        if grid[X][Y]:
                            if R not in Islands:
                                queue.add(R)
                print(f'  Island #{islandNumber}: {size=}')
                answers.append(size)
        print(f'{answers=}')
        return max(answers, default=0)

# NOTE: Accepted on first Submit
# NOTE: Runtime 191 ms Beats 5.14%
# NOTE: Memory 17.31 MB Beats 42.95%
