class Solution:
    @cache
    def legalPos(self, n: int, X: int, Y: int) -> bool:
        return (0 <= X < n) and (0 <= Y < n)

    @cache
    def OOB(self, n: int, X: int, Y: int) -> bool:
        return not self.legalPos(n, X, Y)
    
    directions = (
        (-2, -1), (-1, -2),
        (-2, +1), (-1, +2),
        (+2, -1), (+1, -2),
        (+2, +1), (+1, +2),
    )
    @cache
    def knightMoves(self, cell: Tuple[int,int]) -> List[Tuple[int,int]]:
        (X, Y) = cell
        return [
            (X + I, Y + J)
            for (I, J) in self.directions
        ]

    @cache
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        # if we're off the board: the odds are zero.
        if self.OOB(n, row, column):
            # print(f'{n=},{k=},({row},{column}): [0]')
            return 0.0
        
        # if no moves left: the odds are one.
        if k == 0:
            # print(f'{n=},{k=},({row},{column}): [1]')
            return 1.0
        
        # print(f'{n=},{k=},({row},{column}): ?')
        # otherwise, try every possible move and average them
        nextMoveOdds = [
            self.knightProbability(n, k - 1, X, Y)
            for (X, Y) in self.knightMoves((row, column))
        ]
        # print(f'{n=},{k=},({row},{column}): {nextMoveOdds=}')
        
        return sum(nextMoveOdds) / len(nextMoveOdds)

# NOTE: Accepted on first Submit
# NOTE: Runtime 217 ms Beats 25.83%
# NOTE: Memory 36.82 MB Beats 5.54%
