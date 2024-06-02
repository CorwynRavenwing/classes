class Solution:
    def calculate(self, s: str) -> int:

        def ListToInt(L: List[str]) -> int:
            return int(''.join(L))

        def first_index(operators: str, tokens: List[str|int]) -> int:
            indexes = [
                tokens.index(OPER) if OPER in tokens else None
                for OPER in operators
            ]
            while None in indexes:
                indexes.remove(None)
            return min(indexes) if indexes else None
        
        def calculate(x: int, oper: str, y: int) -> int:
            match oper:
                case '*':
                    return x * y
                case '/':
                    return x // y
                case '+':
                    return x + y
                case '-':
                    return x - y
                case _:
                    raise Exception(f'Invalid operation {oper=} not in "+ - * /"')

        P = list(s.replace(' ', ''))
        # print(f'{P=}')
        new_P = []
        number = []
        for token in P:
            if token in '+-*/':
                if number:
                    new_P.append(ListToInt(number))
                    number = []
                new_P.append(token)
            elif token.isdigit():
                number.append(token)
            else:
                raise Exception(f'unknown {token=}')
        if number:
            new_P.append(ListToInt(number))
            number = []
        P = new_P
        # print(f'{P=}')
        print(f'CALCULATE:')

        while len(P) > 1:
            index = first_index('*/', P)
            if index is not None:
                X = P[index-1]
                OP = P[index]
                Y = P[index+1]
                answer = calculate(X, OP, Y)
                # print(f'{index}: "{P[index]}" {P[index-1:index+2]} -> {answer}')
                # P[index-1:index+2] = [answer]
                del P[index+1]
                del P[index]
                P[index-1] = answer
            else:
                # just consume all the other "+ -" here at once
                X = P[0]
                for i in range(1, len(P), 2):
                    OP = P[i]
                    Y = P[i+1]
                    Z = calculate(X, OP, Y)
                    # print(f'{X} {OP} {Y} -> {Z}')
                    X = Z
                P = [Z]

            # print(f'nothing to do ... ?')
            # print(f'{P=}')

        print(f'DONE:')
        # print(f'{P=}')
        answer = P.pop()
        return answer

