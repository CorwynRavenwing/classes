class Solution:
    def fractionAddition(self, expression: str) -> str:

        MINUS = '-'
        PLUS = '+'
        DIV = '/'
        YES = "yes"
        expr = list(expression)
        print(f'{expr}')
        print(f'NUMBERS:')
        numerals = YES
        while numerals:
            if numerals != YES:
                first = numerals[0]
                beginIndex = expr.index(first)
                accum = 0
                endIndex = beginIndex
                while expr[endIndex].isdigit():
                    accum *= 10
                    accum += int(expr[endIndex])
                    # print(f'{endIndex}: {expr[endIndex]} ({accum})')
                    endIndex += 1
                    if endIndex >= len(expr):
                        # print(f'  OOB')
                        break
                # print(f'[{beginIndex}:{endIndex}] {expr[beginIndex:endIndex]}->{accum}')
                expr[beginIndex:endIndex] = [accum]

            numerals = ''.join([
                E
                for E in expr
                if isinstance(E, str)
                if E not in [MINUS, PLUS, DIV]
            ])
            print(f'{expr}; "{numerals[:3]}"')
        
        print(f'NEGATIVES:')
        while MINUS in expr:
            index = expr.index(MINUS)
            if index + 1 >= len(expr):
                raise Exception(f'"{MINUS}" character at end of expression')
            number = expr[index + 1]
            if not isinstance(number, int):
                actualType = type(number)
                raise Exception(f'"{MINUS}" character needs an int: {actualType=}')
            expr[index] = PLUS
            expr[index + 1] = -number
            # turn "-" (N) into "+" (-N)
            print(f'{expr}')

        if expr[0] == PLUS:
            print(f'LEADING "{PLUS}":')
            del expr[0]
            print(f'{expr}')

        print(f'FRACTIONS:')
        while DIV in expr:
            index = expr.index(DIV)
            if index - 1 < 0:
                raise Exception(f'"{DIV}" character at beginning of expression')
            if index + 1 >= len(expr):
                raise Exception(f'"{DIV}" character at end of expression')
            number1 = expr[index - 1]
            if not isinstance(number1, int):
                actualType1 = type(number1)
                raise Exception(f'"{DIV}" character needs int before: {actualType1=}')
            number2 = expr[index + 1]
            if not isinstance(number2, int):
                actualType2 = type(number2)
                raise Exception(f'"{DIV}" character needs int after: {actualType2=}')
            fraction = (number1, number2)
            # print(f'{expr[index-1:index+2]} -> {fraction}')
            expr[index-1:index+2] = [fraction]
            print(f'{expr}')
        
        print(f'PLUSSES:')
        while PLUS in expr:
            index = expr.index(PLUS)
            frac1 = expr[index - 1]
            if not isinstance(frac1, tuple):
                actualType1 = type(frac1)
                raise Exception(f'"{PLUS}" character needs tuple before: {actualType1=}')
            frac2 = expr[index + 1]
            if not isinstance(frac2, tuple):
                actualType2 = type(frac2)
                raise Exception(f'"{PLUS}" character needs tuple after: {actualType2=}')
            del expr[index]
            print(f'{expr}')

        print(f'ADDITION:')
        while len(expr) > 1:
            (frac1, frac2) = expr[:2]
            print(f'  {frac1} + {frac2}:')
            (N1, D1) = frac1
            (N2, D2) = frac2
            if D1 == D2:
                N3 = N1 + N2
                D3 = D1
            else:
                N3 = (N1 * D2) + (N2 * D1)
                D3 = (D1 * D2)
            if D3 < 0:
                N3 = -N3
                D3 = -D3
            frac3 = (N3, D3)
            print(f'    -> {frac3}')
            expr[:2] = [frac3]

        frac = expr.pop()
        (N, D) = frac
        F = 2
        while F <= D:
            while N % F == 0 and D % F == 0:
                print(f'{N}/{D}')
                print(f'  divide {F}')
                N //= F
                D //= F
            F += 1
        if N == 0:
            print(f'{N}/{D}')
            D = 1
        answer = f'{N}/{D}'
        print(f'{answer=}')
        return answer

