class Solution:
    def numSquares(self, n: int) -> int:

        Squares = {
            X * X
            for X in range(1, int(sqrt(n)) + 1)
        }
        # print(f'{Squares=}')

        answers = {
            square: 1
            for square in Squares
        }
        # answers[N] will contain the lowest possible number of squares
        #   required to add up to this number.
        # for any actual square number, this answer == 1.

        for X in range(1, n+1):
            steps_X = answers[X]
            # print(f'{X}: {steps_X}')
            steps_Y = steps_X + 1
            for square in Squares:
                Y = X + square
                if Y > n:
                    # answers we don't care about
                    continue
                if Y in answers:
                    current_Y = answers[Y]
                    if current_Y < steps_Y:
                        # already a shorter path to Y
                        continue
                # print(f'  +{square} = {Y}: {steps_Y}')
                answers[Y] = steps_Y
        # print(f'\nAnswers:')
        # for (X, A) in sorted(answers.items()):
        #     print(f'  {X}: {A}')
        return answers[n]

# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 2637 ms Beats 43.94%
# NOTE: Memory 17.19 MB Beats 34.28%
