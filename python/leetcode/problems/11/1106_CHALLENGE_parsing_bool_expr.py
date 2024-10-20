class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        tokens = list(expression)

        def lookAhead() -> str:
            nonlocal tokens
            return tokens[0]

        def nextToken() -> str:
            nonlocal tokens
            return tokens.pop(0)

        def parse() -> bool:
            token = nextToken()

            match token:
                case 't':
                    return True
                case 'f':
                    return False
                case '!':
                    return parse_not()
                case '&':
                    return parse_and()
                case '|':
                    return parse_or()
                case _:
                    raise Exception(f'ERROR: invalid {token=} not in "tf!&|"')

        def require(requirement: str) -> bool:
            token = nextToken()
            assert token == requirement
            return True

        def parse_not() -> bool:
            require('(')
            
            answer = parse()
            
            require(')')

            return not answer

        def parse_and() -> bool:
            things = parse_list()
            return all(things)      # ALL == AND

        def parse_or() -> bool:
            things = parse_list()
            return any(things)      # ANY == OR

        def parse_list() -> List[bool]:
            require('(')

            answer = []

            while True:
                answer.append(
                    parse()
                )

                token = lookAhead()
                if token == ')':
                    break
                else:
                    require(',')
            
            require(')')
            
            return answer

        return parse()

# NOTE: Acceptance Rate 60.0% (HARD)
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 67 ms Beats 17.07%
# NOTE: O(N)
# NOTE: Memory 16.84 MB Beats 19.76%
# NOTE: O(N)
