class Solution:
    def solveEquation(self, equation: str) -> str:
        
        # we borrow some code from #592:

        MINUS = '-'
        PLUS = '+'
        EQUAL = '='
        X = 'x'
        YES = "yes"
        NO_SOL = "No solution"
        INF_SOL = "Infinite solutions"

        expr = list(equation)
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
                if E not in [MINUS, PLUS, EQUAL, X]
            ])
            # print(f'{expr}; "{numerals[:3]}"')

        print(f'NEGATIVES:')
        while MINUS in expr:
            index = expr.index(MINUS)
            if index + 1 >= len(expr):
                raise Exception(f'"{MINUS}" character at end of expression')
            number = expr[index + 1]
            if not isinstance(number, int):
                if number == X:
                    # print(f'"{MINUS}" followed by an X: insert 1')
                    expr.insert(index + 1, 1)
                    continue
                else:
                    actualType = type(number)
                    raise Exception(f'"{MINUS}" character needs an int: {actualType=}')
            expr[index] = PLUS
            expr[index + 1] = -number
            # turn "-" (N) into "+" (-N)
            # print(f'{expr}')

        if expr[0] == PLUS:
            print(f'LEADING "{PLUS}", left side:')
            del expr[0]
            # print(f'{expr}')
        equal_index = expr.index(EQUAL)
        right_side_index = equal_index + 1
        if right_side_index < len(expr):
            if expr[right_side_index] == PLUS:
                print(f'LEADING "{PLUS}", right side:')
                del expr[right_side_index]
                # print(f'{expr}')

        print(f"X'S:")
        while X in expr:
            index = expr.index(X)
            if index > 0:
                number = expr[index - 1]
                if isinstance(number, int):
                    # print(f'X preceeded by int')
                    x_object = (number, X)
                    expr[index] = x_object  # update first, delete second,
                    del expr[index - 1]     # or the indexes will be wrong
                    # print(f'{expr}')
                    continue
                # # The following case is actually handled during MINUS parsing
                # elif number == MINUS:
                #     print(f'X preceeded by MINUS')
                #     number = -1
                #     x_object = (number, X)
                #     expr[index] = x_object  # update first, delete second,
                #     del expr[index - 1]     # or the indexes will be wrong
                #     print(f'{expr}')
                #     continue
            print(f'X by itself')
            number = 1
            x_object = (number, X)
            expr[index] = x_object
            # print(f'{expr}')
        
        print(f'PLUSSES:')
        while PLUS in expr:
            index = expr.index(PLUS)
            obj1 = expr[index - 1]
            if (not isinstance(obj1, int)) and (not isinstance(obj1, tuple)):
                actualType1 = type(obj1)
                raise Exception(f'"{PLUS}" character needs int or tuple before: {actualType1=}')
            obj2 = expr[index + 1]
            if (not isinstance(obj2, int)) and (not isinstance(obj2, tuple)):
                actualType2 = type(obj2)
                raise Exception(f'"{PLUS}" character needs int or tuple after: {actualType2=}')
            del expr[index]
            # print(f'{expr}')
        
        print(f'COLLECT TERMS:')
        index = 0
        while index < len(expr):
            equal_index = expr.index(EQUAL)
            this = expr[index]
            if index < equal_index:
                # print(f'  {index}: {this} (Left)')
                if isinstance(this, tuple):
                    # print(f'    an X on the left: keep it.')
                    index += 1
                    continue
                elif isinstance(this, int):
                    # print(f'    an int on the left: move to right side.')
                    del expr[index]
                    expr.append(-this)
                    # repeat index
            elif index > equal_index:
                # print(f'  {index}: {this} (Right)')
                if isinstance(this, int):
                    # print(f'    an int on the right: keep it.')
                    index += 1
                    continue
                elif isinstance(this, tuple):
                    # print(f'    an X on the right: move to left side.')
                    (number, ignoreX) = this
                    assert ignoreX == X
                    neg_this = (-number, X)
                    del expr[index]              # delete first, insert second
                    expr.insert(equal_index, neg_this)  # or break the indexes
                    # repeat index
            else:
                # print(f'  equal sign')
                index += 1
                continue
            # print(f'{expr}')

        equal_index = expr.index(EQUAL)
        if equal_index == 0:
            # print(f'No X term on left: add zero')
            zeroX = (0, X)
            expr.insert(0, zeroX)
            # print(f'{expr}')
        if expr[-1] == EQUAL:
            # print(f'No integer term on right: add zero')
            expr.append(0)
            # print(f'{expr}')
        
        print(f'COMBINE TERMS:')
        while len(expr) > 3:
            equal_index = expr.index(EQUAL)
            if equal_index > 1:
                # print(f'combine terms on left')
                (X1, X2) = expr[:2]
                (val1, ignore1) = X1
                assert ignore1 == X
                (val2, ignore2) = X2
                assert ignore2 == X
                newX = (val1 + val2, X)
                # print(f'  {X1} + {X2} -> {newX}')
                expr[:2] = [newX]
            else:
                # print(f'combine terms on right')
                (val1, val2) = expr[-2:]
                newVal = val1 + val2
                # print(f'  {val1} + {val2} -> {newVal}')
                expr[-2:] = [newVal]
            # print(f'{expr}')

        print(f'DIVIDE:')
        X1 = expr[0]
        (val1, ignore1) = X1
        val2 = expr[-1]
        # print(f'clean up {val1=} {val2=}')
        if val1 not in [0, 1]:
            print(f'  divide by {val1}')
            newX = (val1 // val1, X)
            assert val2 % val1 == 0
            newVal = val2 // val1
            expr[0] = newX
            expr[-1] = newVal
            # print(f'{expr}')
        else:
            print(f'  X coefficient ({val1}) is already 0 or 1')
            # print(f'{expr}')

        print(f'SOLVE:')
        X1 = expr[0]
        (val1, ignore1) = X1
        val2 = expr[-1]
        assert val1 in [0, 1]
        if val1 == 1:
            # 1x = N
            return f"x={val2}"
        elif val2 == 0:
            # 0x = 0
            return INF_SOL
        else:
            # 0x = N
            return NO_SOL

