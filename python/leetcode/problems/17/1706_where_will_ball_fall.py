class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        def moveBalls(balls: List[int], row: List[int]) -> List[int]:
            fixRow = [1] + row + [-1]   # add walls
            pins = [
                (
                    (
                        -1
                        if (before != 1)
                        else None
                    )
                    if this == -1
                    else
                    (
                        1
                        if (after != -1)
                        else None
                    )
                    if this == 1
                    else
                    f'ERROR {this=}'
                )
                for (before, this, after) in zip(fixRow, fixRow[1:], fixRow[2:])
            ]
            print(f'  {row=}')
            print(f'  {pins=}')
            newBalls = []
            for B in balls:
                # print(f'  {B=}')
                if B != -1:
                    P = pins[B]
                    if P is None:
                        B = -1
                    else:
                        B += P
                # print(f'  -> {B}')
                newBalls.append(B)
            return newBalls
        
        grid_M = len(grid)
        grid_N = len(grid[0])

        balls = list(range(0, grid_N))
        print(f'B: {balls=}')
        for i, row in enumerate(grid):
            balls = moveBalls(balls, row)
            print(f'{i}: {balls=}')
        return balls

