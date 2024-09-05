class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacleX = {}
        for (X, Y) in obstacles:
            obstacleX.setdefault(X, set())
            obstacleX[X].add(Y)
        print(f'{obstacleX=}')
        origin = (0, 0)
        position = origin
        direction = (0, +1)     # north
        maxdist = 0

        def checkDistance() -> None:
            nonlocal position
            nonlocal maxdist
            (X, Y) = position
            distance = (X * X) + (Y * Y)
            # magically subtract origin
            # magically get absolute value by squaring
            if maxdist < distance:
                print(f'New max distance: {position} = {distance}')
                maxdist = distance
            return

        def turn(cmd: int) -> None:
            nonlocal direction
            directions = [
                (0, +1),    # North
                (+1, 0),    # East
                (0, -1),    # South
                (-1, 0),    # West
            ]
            dirIndex = directions.index(direction)
            cmd_to_delta = {
                -2: -1,     # -2: turn left 90 degrees
                -1: +1,     # -1: turn right 90 degrees
            }
            delta = cmd_to_delta[cmd]
            dirIndex += delta
            dirIndex %= len(directions)
            direction = directions[dirIndex]
            print(f'{cmd}: turn {direction}')
            return

        def move(cmd: int) -> None:
            nonlocal direction
            nonlocal position
            nonlocal obstacleX
            for i in range(cmd):
                (X, Y) = position
                (A, B) = direction
                nextPos = (X + A, Y + B)
                (nX, nY) = nextPos
                if nX in obstacleX:
                    if nY in obstacleX[nX]:
                        print(f'{i+1}/{cmd}: {position} ({nextPos} BLOCKED)')
                        break
                position = nextPos
                print(f'{i+1}/{cmd}: {position}')
                checkDistance()

        for cmd in commands:
            if cmd < 0:
                turn(cmd)
            else:
                move(cmd)
        return maxdist

# NOTE: Runtime 452 ms Beats 5.14%
# NOTE: Memory 23.51 MB Beats 12.86%
