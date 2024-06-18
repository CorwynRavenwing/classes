from collections import Counter

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        # new, logical method (53 ms)
        moveCount = Counter(moves)

        return (
            (
                moveCount['L'] == moveCount['R']
            ) and (
                moveCount['U'] == moveCount['D']
            )
        )

        # original, by-hand method (122 ms)
        def next_pos(pos: Tuple[int,int], direction: str) -> Tuple[int,int]:
            (i, j) = pos
            moves = {
                'U': (i, j-1),
                'D': (i, j+1),
                'L': (i-1, j),
                'R': (i+1, j),
            }
            return moves[direction]
        
        origin = (0, 0)
        pos = origin
        for move in moves:
            pos = next_pos(pos, move)
        
        return (pos == origin)

