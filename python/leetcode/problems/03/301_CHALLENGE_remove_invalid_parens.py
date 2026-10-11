class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        
        # we borrow some code from #678:
        def isValidString(s: str) -> bool:
            possible = {0}
            # here I'm literally only keeping track of the number of open parens.
            for ch in s:
                # print(f'"{ch}": {possible}')
                new_possible = set()
                for P in possible:
                    if P < 0:
                        # too many close parens: throw out this P
                        continue
                    if ch == '(':
                        new_possible.add(P + 1)  # open one paren
                    elif ch == ')':
                        new_possible.add(P - 1)  # close one paren
                    # no '*' match
                    else:
                        new_possible.add(P)      # empty string
                possible = new_possible
            # end of string
            # print(f'end: {possible}')
            if 0 in possible:
                # print(f'all parens closed')
                return True
            else:
                # print(f'no successful parses')
                return False
        
        # for S in ["(a())()","(a)()()"]:
        #     print(f'DEBUG: {S}: valid={isValidString(S)}')

        # return ['die']

        if isValidString(s):
            print(f'STOP: string "s" is valid')
            return [s]
        
        def allChildren(T: str) -> List[str]:
            print(f'  allChildren("{T}"):')
            for i, ch in enumerate(T):
                if ch == '(' or ch == ')':
                    answer = T[:i] + T[i+1:]
                    print(f'    {i=} {answer}')
                    yield answer
            return

        queue = {s,}
        while queue:
            print(f'Q={len(queue)}')
            valid = set()
            print(f':check valid')
            for T in queue:
                V = isValidString(T)
                print(f'  {T=} {V=}')
                if V:
                    valid.add(T)
            if valid:
                print(f'STOP: found some valid strings')
                return tuple(valid)
            newQ = set()
            print(f':make children')
            for T in queue:
                # print(f'  {T=}')
                for child in allChildren(T):
                    # print(f'    {child=}')
                    newQ.add(child)
            queue = newQ
        
        return ['should', 'not', 'get', 'here']

# NOTE: Acceptance Rate 50.3% (HARD)

# NOTE: Accepted on third Run (copied code answers wrong question)
# NOTE: Accepted on first Submit
# NOTE: Runtime 271 ms Beats 36.31%
# NOTE: Memory 19.66 MB Beats 51.91%
