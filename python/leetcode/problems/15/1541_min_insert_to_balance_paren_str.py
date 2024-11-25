class Solution:
    def minInsertions(self, s: str) -> int:
        
        # we want to differentiate between single close parens
        # and double (usable) close parens
        s = s.replace('))', ']')
        # ']' represents two ')': therefore ')' is a singleton
        openParens = 0

        answer = 0

        for char in s:
            # print(f'{answer}: {openParens=} {char=}')

            match char:
                case '(':
                    openParens += 1
                case ']':
                    if not openParens:
                        # print(f'  prepend open')
                        answer += 1
                    else:
                        openParens -= 1
                case ')':
                    if not openParens:
                        # print(f'  prepend open')
                        answer += 1
                    else:
                        openParens -= 1
                    # print(f'  add second close')
                    answer += 1
                case _:
                    raise Exception(f'Error: invalid character {char=}')
        
        while openParens:
            # print(f'Leftover open -> add two closes')
            answer += 2
            openParens -= 1
        
        return answer

# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 53 ms Beats 73.36%
# NOTE: Memory 17.13 MB Beats 73.92%
