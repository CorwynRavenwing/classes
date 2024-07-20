class Solution:
    def minFlips(self, s: str) -> int:

        # we borrow some code from #1864

        def calculateAnswer(s: str) -> int:
            diffs_even = 0
            diffs_odds = 0
            for index, digit in enumerate(s):
                if index % 2 == 0:
                    # even index
                    digit_even = '0'
                else:
                    # odd index
                    digit_even = '1'
                if digit == digit_even:
                    diffs_odds += 1
                else:
                    diffs_even += 1
                # therefore d_e + d_o === len(s), and we really only need to calculate one of them

            available_diffs = [
                diffs_even,
                diffs_odds,
            ]
            # print(f'{diffs_even=} {diffs_odds=} {available_diffs=}')
            return available_diffs

        best_answers = []
        best_answers.extend(calculateAnswer(s))
        # try all possible rotations:
        for i in range(len(s)):
            T = s[i:] + s[:i]     # rotate by "i"
            best_answers.extend(calculateAnswer(T))
        
        print(f'{best_answers=}')

        return min(best_answers)
# NOTE: Time Limit Exceeded for large inputs
