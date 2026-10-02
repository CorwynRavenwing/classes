class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        possibles = [
            ('', 0, n)
        ]
        answers = []
        while possibles:
            print(f'L={len(possibles)}')
            P = possibles.pop(0)
            print(f'  {P=}')
            (answer, to_close, to_open) = P
            if to_open:
                print('    +open')
                possibles.append(
                    (answer + '(', to_close + 1, to_open - 1)
                )
            if to_close:
                print('    +close')
                possibles.append(
                    (answer + ')', to_close - 1, to_open)
                )
            if (not to_open) and (not to_close):
                print('    +answer')
                answers.append(answer)
                continue
        return answers

# NOTE: Acceptance Rate 79.2% (medium)

# NOTE: re-ran for challenge:
# NOTE: Runtime 17 ms Beats 5.29%
# NOTE: Memory 19.40 MB Beats 36.93%
