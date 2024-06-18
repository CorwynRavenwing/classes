class Solution:
    def checkValidString(self, s: str) -> bool:

        possible = {0}
        # here I'm literally only keeping track of the number of open parens.
        for ch in s:
            print(f'"{ch}": {possible}')
            new_possible = set()
            for P in possible:
                if P < 0:
                    # too many close parens: throw out this P
                    continue
                if ch == '(':
                    new_possible.add(P + 1)  # open one paren
                if ch == ')':
                    new_possible.add(P - 1)  # close one paren
                if ch == '*':
                    new_possible.add(P + 1)  # open one paren
                    new_possible.add(P)      # empty string
                    new_possible.add(P - 1)  # close one paren
            possible = new_possible
        # end of string
        print(f'end: {possible}')
        if 0 in possible:
            print(f'all parens closed')
            return True
        else:
            print(f'no successful parses')
            return False

