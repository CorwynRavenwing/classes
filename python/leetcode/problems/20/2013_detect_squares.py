class DetectSquares:

    def __init__(self):
        self.pointCounts = {}   # Dict[Tuple[int,int]: int]
        self.YsOnX = {}         # Dict[int: Set[int]]
        self.XsOnY = {}

    def add(self, point: List[int]) -> None:
        (X, Y) = point
        point = tuple(point)
        print(f'add({point})')
        self.pointCounts.setdefault(point, 0)
        self.pointCounts[point] += 1
        self.YsOnX.setdefault(X, set())
        self.YsOnX[X].add(Y)
        self.XsOnY.setdefault(Y, set())
        self.XsOnY[Y].add(X)
        
    def count(self, point: List[int]) -> int:
        (X, Y) = point
        point = tuple(point)
        print(f'count({point})')
        if X not in self.YsOnX:
            print(f'  {X=} not found')
            print(f'  DEBUG {self.YsOnX=}')
            return 0
        else:
            Ys = self.YsOnX[X]
        if Y not in self.XsOnY:
            print(f'  {Y=} not found')
            print(f'  DEBUG {self.XsOnY=}')
            return 0
        else:
            Xs = self.XsOnY[Y]
        answer = 0
        for X2 in Xs:
            A = (X2, Y)
            Acount = self.pointCounts[A]    # will exist b/c X2 in Xs
            size = abs(X - X2)
            if size == 0:
                print(f'  Skip {size=}')
                continue
            else:
                print(f'  Check for {size=}')
            for Y2 in [Y - size, Y + size]:
                if Y2 not in Ys:
                    # print(f'    No match at {Y2=}')
                    continue
                B = (X, Y2)
                Bcount = self.pointCounts[B]    # will exist b/c Y2 in Ys
                C = (X2, Y2)
                if C not in self.pointCounts:
                    print(f'    No match at point {C=}')
                    continue
                else:
                    Ccount = self.pointCounts[C]    # will exist b/c we just checked
                    print(f'    SQUARE {point} {A} {B} {C} : [{Acount},{Bcount},{Ccount}]')
                    product = Acount * Bcount * Ccount
                    print(f'      {product=}')
                    answer += product
        print(f'count({point}): RETURN {answer=}')
        return answer

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
