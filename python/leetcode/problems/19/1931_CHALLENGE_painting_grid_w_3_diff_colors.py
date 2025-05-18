class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        
        mod = 10 ** 9 + 7

        # SHORTCUT 1: n (width in columns) can be very large (1000),
        # while m (height in rows) can be only 5.
        # Therefore, we pass *column* data (up to 5 in size)
        # into a DP for each *row* (up to 1000 times).

        # SHORTCUT 2: for each column, there are only a maximum of
        # 3 * 2 * 2 * 2 * 2
        # = 48 possible patterns
        #   3 === possible colors for cell 1
        #   2 === colors we didn't just use
        # Therefore, we precompute them.

        def all_patterns(local_M) -> List[str]:

            def generate_patterns(size, prior='') -> List[str]:
                if size == 0:
                    yield ''
                    return
                for color in 'RGB':
                    if color == prior:
                        continue
                    for pattern in generate_patterns(size - 1, color):
                        yield color + pattern
                return
            
            return tuple(generate_patterns(local_M))
        
        possible_patterns = all_patterns(m)
        print(f'Found {len(possible_patterns)} patterns')
        # for P in possible_patterns:
        #     print(f'  {P}')
        
        # @cache    # actually makes it slightly worse!
        def patterns_acceptable(pattern, prior_pattern: str) -> bool:
            if not prior_pattern:
                return True
            for (A, B) in zip(pattern, prior_pattern):
                if A == B:
                    return False
            return True

        @cache
        def patterns_that_may_follow(prior_pattern: str) -> List[str]:
            # nonlocal possible_patterns
            allowed = lambda pattern: patterns_acceptable(pattern, prior_pattern)
            return tuple(
                filter(
                    allowed,
                    possible_patterns
                )
            )

        @cache
        def DP(col: int, prior_pattern: str) -> int:
            indent = '' * (5 - col)
            # print(f'{indent}DP({col},{prior_pattern}): begin')
            if col == 0:
                return 1
            allowed_patterns = patterns_that_may_follow(prior_pattern)
            answers = [
                DP(col - 1, pattern)
                for pattern in allowed_patterns
            ]
            # print(f'{indent}DP({col},{prior_pattern}): {answers=}')
            answer = sum(answers) % mod
            # print(f'{indent}DP({col},{prior_pattern}): {answer =}')
            return answer

        answer = DP(n, '')

        return answer % mod

# NOTE: Acceptance Rate 58.5% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 552 ms Beats 38.89%
# NOTE: Memory 35.69 MB Beats 27.78%
