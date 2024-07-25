class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.directionDelta = {
            'East': (+1, 0),
            'North': (0, +1),
            'West': (-1, 0),
            'South': (0, -1),
        }
        self.direction = 'East'
        self.position = (0,0)

        self.perimeter = None
        self.cachedStates = []
        self.state = None
    
    def turn(self) -> None:
        dirList = tuple(self.directionDelta.keys())
        dirIndex = dirList.index(self.direction)
        dirIndex += 1
        dirIndex %= len(dirList)
        self.direction = dirList[dirIndex]
        print(f'  now facing {self.direction}')
        return
    
    def legalPos(self, position: Tuple[int,int]) -> bool:
        (X, Y) = position
        return (0 <= X < self.width) and (0 <= Y < self.height)

    def OOB(self, position: Tuple[int,int]) -> bool:
        return not self.legalPos(position)
    
    def nextPosition(self) -> Tuple[int,int]:
        (X, Y) = self.position
        delta = self.directionDelta[self.direction]
        (I, J) = delta
        return (X + I, Y + J)
    
    def turnIfNextPositionOOB(self) -> None:
        pos = self.nextPosition()
        if self.OOB(pos):
            print(f'OOB {pos}: turning')
            self.turn()
        return

    def moveForward(self) -> None:
        pos = self.nextPosition()
        self.position = pos
        print(f'moving to {pos}')
        return

    def quickStep(self, num: int) -> None:
        print(f'Quick way:')
        print(f'  old {num=} {self.state=}')
        num %= self.perimeter
        self.state += num
        self.state %= self.perimeter
        print(f'  new {num=} {self.state=}')
        state = self.cachedStates[self.state]
        print(f'  jump to {state=}')
        (self.direction, self.position) = state
        return

    def step(self, num: int) -> None:
        print(f'step({num})')
        if self.perimeter:
            self.quickStep(num)
            return
        
        while num:
            num -= 1
            self.turnIfNextPositionOOB()
            self.moveForward()
            state = (self.direction, self.position)
            if (state not in self.cachedStates):
                self.cachedStates.append(state)
                continue
            else:
                self.state = self.cachedStates.index(state)
                self.perimeter = len(self.cachedStates)
                print(f'Now ready to do Quick Way for remaining {num}:')
                self.quickStep(num)
                return
        return

    def getPos(self) -> List[int]:
        return self.position

    def getDir(self) -> str:
        return self.direction

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

# NOTE: Runtime 467 ms Beats 25.40%
# NOTE: Memory 21.77 MB Beats 11.11%
