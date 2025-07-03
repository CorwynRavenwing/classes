class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        
        mod = 10 ** 9 + 7

        # we borrow some code from #3330:

        s = word

        letters_and_counts = [
            (key, len(tuple(values)))
            for key, values in groupby(s)
        ]
        # print(f'{letters_and_counts=}')

        possible_additions = [
            count - 1
            for letter, count in letters_and_counts
            if count > 1
        ]
        # print(f'{possible_additions=}')

        @cache
        def DP(points: int, index: int) -> int:
            # print(f'DP({points},{index}):')
            if points == 0:
                # print(f'  0 -> 1')
                return 1
            assert points > 0
            try:
                possible = possible_additions[index]
            except IndexError:
                # print(f'  EOF -> 1')
                return 1
            possible = min(possible, points)
            answers = [
                DP(
                    points - pick_this_time,
                    index + 1
                )
                for pick_this_time in range(0, possible + 1)
            ]
            # print(f'DP({points},{index}): {answers}')
            answer = sum(answers)
            # print(f'  {answer}')
            return answer % mod

        answer = DP(
            len(word) - k,
            0
        )

        return answer % mod

# NOTE: Acceptance Rate 16.4% (HARD)

# NOTE: Time Limit Exceeded for large inputs (#814)
