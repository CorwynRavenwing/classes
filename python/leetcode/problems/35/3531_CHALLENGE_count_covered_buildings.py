class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        
        # make each building hashable
        buildings = tuple(map(tuple, buildings))

        uncovered = set()

        groupByX = {}
        groupByY = {}
        for B in buildings:
            (X, Y) = B
            # print(f'{B}')
            groupByX.setdefault(X, [])
            groupByY.setdefault(Y, [])
            groupByX[X].append(B)
            groupByY[Y].append(B)
        # print(f'{groupByX=}')
        # print(f'{groupByY=}')

        BY_X = lambda B: (B[0])
        BY_Y = lambda B: (B[1])

        for X, buildingsX in groupByX.items():
            buildingsX.sort(key=BY_Y)
            # print(f'{X=} {buildingsX}')
            A = buildingsX[0]
            B = buildingsX[-1]
            # print(f'  delete {A} {B}')
            uncovered.add(A)
            uncovered.add(B)

        for Y, buildingsY in groupByY.items():
            buildingsY.sort(key=BY_X)
            # print(f'{Y=} {buildingsY}')
            A = buildingsY[0]
            B = buildingsY[-1]
            # print(f'  delete {A} {B}')
            uncovered.add(A)
            uncovered.add(B)
        
        covered = set(buildings) - uncovered
        return len(covered)

# NOTE: Acceptance Rate 38.5% (medium)

# NOTE: Accepted on third Run (variable-name typos)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 679 ms Beats 49.58%
# NOTE: Memory 75.09 MB Beats 9.24%
