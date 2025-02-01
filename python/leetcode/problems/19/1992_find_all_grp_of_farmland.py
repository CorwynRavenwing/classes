class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        M = len(land)
        N = len(land[0])

        def getValue(X: int, Y: int) -> int:
            try:
                return land[X][Y]
            except IndexError:
                # OOB: not farmland
                return 0

        def isTopLeft(X: int, Y: int) -> bool:
            up = getValue(X_TL - 1, Y_TL)
            left = getValue(X_TL, Y_TL - 1)
            isTop = ((up == 0) or (X == 0))
            isLeft = ((left == 0) or (Y == 0))
            return (
                isTop and isLeft
            )
        
        def findBottomRight(X: int, Y: int) -> Tuple[int,int]:
            while getValue(X + 1, Y) == 1:
                X += 1
            while getValue(X, Y + 1) == 1:
                Y += 1
            return (X, Y)
                
        answers = []
        for X_TL in range(M):
            for Y_TL in range(N):
                print(f'({X_TL},{Y_TL})')
                value = getValue(X_TL, Y_TL)
                if value == 0:
                    print(f'  (forest)')
                    continue
                if not isTopLeft(X_TL, Y_TL):
                    print(f'  (interior)')
                    continue
                (X_BR, Y_BR) = findBottomRight(X_TL, Y_TL)
                answers.append(
                    (X_TL, Y_TL, X_BR, Y_BR)
                )
        return answers

# NOTE: Accepted on second Run (literal edge case: top or left edge)
# NOTE: Accepted on first Submit
# NOTE: Runtime 524 ms Beats 5.93%
# NOTE: Memory 30.42 MB Beats 96.86%
