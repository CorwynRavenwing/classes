class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:

        M = len(grid)
        N = len(grid[0])
        target = (M - 1, N - 1)

        # print(f'DEBUG: {grid=}')
        
        @cache
        def DP(x: int, y: int, k_remain: int) -> int:
            # print(f'DP(({x},{y}),{k_remain})')
            try:
                value = grid[x][y]
            except IndexError:
                # print(f'  OOB')
                return None
            # print(f'  {value=}')
            cost = (
                1 if value
                else 0
            )
            k_remain -= cost
            if k_remain < 0:
                # print(f'  NO: {cost=} {k_remain=}')
                return None
            if (x, y) == target:
                # print(f'  YES: {value=}')
                return value
            answers = [
                DP(x + 1, y, k_remain),
                DP(x, y + 1, k_remain),
            ]
            # print(f'DP(({x},{y}),{k_remain}): {answers=}')
            while None in answers:
                answers.remove(None)
            if not answers:
                # print(f'DP(({x},{y}),{k_remain}): NO {answers=}')
                return None
            answer = value + max(answers)
            # print(f'DP(({x},{y}),{k_remain}): YES {answer}')
            return answer
        
        answer = DP(0, 0, k)

        return (
            -1 if answer is None
            else answer
        )

# NOTE: Acceptance Rate 38.4% (medium)

# NOTE: Incomplete: TLE without cache, MLE with cache
