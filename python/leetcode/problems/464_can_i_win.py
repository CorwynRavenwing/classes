class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        cache_positionWins = {}
        def positionWins(state: Tuple[int, List[int]], depth=0) -> bool:
            margin = "  " * depth
            # print(margin + f'pw({state}):')
            if state in cache_positionWins:
                answer = cache_positionWins[state]
                # print(margin + f'..cache hit {answer}')
                return answer
            (points, moves) = state
            
            if sum(moves) < points:
                print(margin + f'..not enough points to win: you lose')
                answer = False
                cache_positionWins[state] = answer
                return answer

            if not moves:
                print(margin + f'..no moves left: lose')
                answer = False
                cache_positionWins[state] = answer
                return answer

            if max(moves) >= points:
                print(margin + f'..move {max(moves)} wins!')
                answer = True
                cache_positionWins[state] = answer
                return answer
            
            any_opponent_losses = False
            for move in moves:
                # print(margin + f'..try {move=}')
                still_available_moves = list(moves)   # copy, allow mutation
                still_available_moves.remove(move)
                new_state = (
                    points - move,
                    tuple(still_available_moves)
                )
                if not positionWins(new_state, depth+1):
                    # print(margin + f'....opponent loses!')
                    any_opponent_losses = True
                    break   # stop looking
                # else:
                #     print(margin + f'....opponent wins')
            if any_opponent_losses:
                # print(margin + f'..opponent can lose!')
                answer = True
            else:
                # print(margin + f'..opponent always wins: you lose')
                answer = False

            cache_positionWins[state] = answer
            return answer
        
        choosableIntegers = tuple(range(1, maxChoosableInteger+1))
        initialState = (desiredTotal, choosableIntegers)
        return positionWins(initialState)

