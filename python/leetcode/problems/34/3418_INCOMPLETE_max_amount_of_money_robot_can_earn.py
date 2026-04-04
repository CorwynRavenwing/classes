class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        
        FAIL = float('-inf')
        M = len(coins)
        N = len(coins[0])

        # 0: call this at each step
        @cache
        def DP(x: int, y: int, bullets: int) -> int:
            try:
                value = coins[x][y]
            except IndexError:
                # print(f'DP({x},{y},{bullets}): OOB')
                return FAIL
            # print(f'DP({x},{y},{bullets}): start')
            answers = [
                DP_robbed(x, y, bullets),
                DP_neutralize(x, y, bullets),
            ]
            answer = max(answers)
            # print(f'DP({x},{y},{bullets}): {answer} <- {answers}')
            return answer
        
        # 1: choose whether to be robbed (if negative),
        #    or to neutralize this robber
        # @cache
        def DP_robbed(x: int, y: int, bullets: int) -> int:
            # print(f'  DP_robbed({x},{y},{bullets})')
            try:
                value = coins[x][y]
            except IndexError:
                # print(f'  DP_robbed({x},{y},{bullets}): OOB')
                return FAIL
            answer = value + DP_move(x, y, bullets)
            # print(f'  DP_robbed({x},{y},{bullets}): {value} -> {answer}')
            return answer

        # @cache
        def DP_neutralize(x: int, y: int, bullets: int) -> int:
            # print(f'  DP_neutralize({x},{y},{bullets})')
            if bullets <= 0:
                # out of bullets
                # print(f'  DP_neutralize({x},{y},{bullets}): oob')
                return FAIL
            try:
                value = coins[x][y]
            except IndexError:
                # print(f'  DP_neutralize({x},{y},{bullets}): OOB')
                return FAIL
            if value >= 0:
                # cannot neutralize a nonexistent robber
                # print(f'  DP_neutralize({x},{y},{bullets}): norob ({value=})')
                return FAIL
            answer = 0 + DP_move(x, y, bullets - 1)
            # print(f'  DP_neutralize({x},{y},{bullets}): {answer}')
            return answer

        # 2: then call this to move to the next location
        @cache
        def DP_move(x: int, y: int, bullets: int) -> int:
            # print(f'  DP_move({x},{y},{bullets})')
            if (x, y) == (M - 1, N - 1):
                # print(f'    DONE')
                return 0
            answers = [
                # 3: choose whether to move to next X or Y
                DP(x + 1, y    , bullets),
                DP(x    , y + 1, bullets),
            ]
            answer = max(answers)
            # print(f'  DP_move({x},{y},{bullets}): {answer} <- {answers}')
            return answer
        
        answer = DP(0, 0, 2)
        # print(f'Final {answer=}')
        return answer

# NOTE: Acceptance Rate 29.8% (medium)

# NOTE: Memory Exceeded for large inputs
