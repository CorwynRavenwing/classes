class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        # first, score all "()" as "1":
        s = s.replace('()', '1')
        print(f'{s=}')

        stack = [0]
        print(f'^: {stack}')
        for char in s:

            match char:
                case '(':
                    stack.append(0)
                case '1':
                    stack[-1] += 1
                case ')':
                    A = stack.pop(-1)
                    stack[-1] += 2 * A
                case _:
                    raise Exception(f'Error: invalid {char=}, not in "()1"')
            
            print(f'{char}: {stack}')
        
        assert len(stack) == 1
        return stack.pop()

# NOTE: Accepted on second Run (first was one-char typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.77 MB Beats 5.28%
