class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        
        M = len(grid)
        N = len(grid[0])

        print(f'{M=} x {N=}')
        if M * N > 70000:
            return -999

        def valueAt(cell: Tuple[int,int]) -> int:
            (X, Y) = cell
            return grid[X][Y]

        def movesFrom(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            (X, Y) = cell
            answers = [
                (newX, Y)
                for newX in range(X + 1, M)
            ] + [
                (X, newY)
                for newY in range(Y + 1, N)
            ]
            # print(f'movesFrom({cell}): {answers}')
            return answers

        BSSA_cache = {}
        def bestScoreStartingAt(cell: Tuple[int,int], allowNotMoving: bool, depth=0) -> int:
            # margin = '  ' * depth
            # print(f'{margin}BSSA({cell},{allowNotMoving})')
            if allowNotMoving:
                bs = bestScoreStartingAt(cell, False, depth)
                if bs is None:
                    return 0
                else:
                    return max(0, bs)

            if cell in BSSA_cache:
                answer = BSSA_cache[cell]
                # print(f'{margin}  cache hit {answer}')
                return answer

            # print(f'{margin}BSSA({cell},{allowNotMoving})')
            c1 = valueAt(cell)
            answers = []
            for newCell in movesFrom(cell):
                c2 = valueAt(newCell)
                extra = bestScoreStartingAt(newCell, True, depth+1)
                score = c2 - c1 + extra
                # print(f'{margin}  BSSA({cell},{allowNotMoving}): {score} = {c2} - {c1} + {extra}')
                answers.append(score)
            # print(f'{margin}  BSSA({cell},{allowNotMoving}): {answers=}')
            answer = max(answers, default=None)
            
            BSSA_cache[cell] = answer
            # print(f'{margin}  BSSA({cell},{allowNotMoving}): {answer}')
            return answer
        
        answers = [
            bestScoreStartingAt((X, Y), False)
            for X in range(M)
            for Y in range(N)
        ]
        # print(f'{answers=}')
        if None in answers:
            answers.remove(None)
        return max(answers)

# NOTE: this times out for large inputs.
# NOTE: I just thought of a much better method.
