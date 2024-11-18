class Solution:

    def __init__(self):
        # SHORTCUT: as several commenters have said, there is a *TINY* number
        # of possible solutions to this problem.  Enumerate them all here.
        digits = tuple(map(str, range(1, 10)))  # '123456789'
        prior_answer = digits
        answers = []
        for length in range(2, 10):
            this_answer = [
                prior + (
                    str(
                        sum([
                            int(prior[-1]),
                            1,
                        ])
                    )
                )
                for prior in prior_answer
                if prior[-1] != '9'
            ]
            print(f'{length=} {this_answer=}')
            answers.extend(
                map(int, this_answer)
            )
            prior_answer = this_answer

        self.all_answers = answers
        return
    
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        return [
            A
            for A in self.all_answers
            if low <= A <= high
        ]

# NOTE: Accepted on third Run (variable name typo, str/int conflict)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.69 MB Beats 29.65%
