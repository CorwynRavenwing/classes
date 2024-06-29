class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = 0
        errors = 0
        for C in s:
            if C == '(':
                stack += 1
                print(f'Open paren, {stack=}')
            elif C == ')':
                if stack:
                    stack -= 1
                    print(f'Close paren, {stack=}')
                else:
                    errors += 1
                    print(f'Unbalanced close paren, {errors=}')
            else:
                raise Exception(f'Invalid character {C=}')
        if stack:
            errors += stack
            print(f'{stack} unbalanced open parens, {errors=}')
        return errors

