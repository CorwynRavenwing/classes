class Solution:
    def countOfAtoms(self, formula: str) -> str:

        def parseAtomFormula(formula: str) -> List[str]:
            answer = []
            inprog = None
            for F in formula:
                # print(f'{F=}')
                if F.isupper():
                    # begin an element
                    # print(f'  store "{inprog}"')
                    answer.append(inprog)
                    inprog = F
                    # print(f'  begin "{inprog}"')
                    continue
                if F.islower():
                    # continue an element
                    if inprog is None:
                        print(f'ERROR! cant continue nonexistent element.  {inprog=} {F=}')
                        answer.append('ERROR!')
                        return answer
                    inprog += F
                    # print(f'  grow "{inprog}"')
                    continue
                if F in '()':
                    # opening or closing parenthesis
                    # print(f'  store "{inprog}"')
                    answer.append(inprog)
                    # print(f'  store paren "{F}"')
                    answer.append(F)
                    inprog = None
                    continue
                if F.isdigit():
                    # a number
                    if inprog is None:
                        inprog = ''
                    elif not inprog.isdigit():
                        # print(f'  store "{inprog}"')
                        answer.append(inprog)
                        inprog = ''
                    # print(f'  grow digit "{F}"')
                    inprog += F
                    continue
            # print(f'  store "{inprog}"')
            answer.append(inprog)
            while None in answer:
                answer.remove(None)
            return answer
        
        def multiplyAtoms(parsed: List[str]) -> List[str]:
            answer = parsed
            # print(f'{answer=}')
            while True:
                changes = False
                lastOpenParenIndex = None
                for i, P in enumerate(answer):
                    if P == '(':
                        lastOpenParenIndex = i
                        continue
                    if P.isdigit():
                        # following line will fail if a number is the first object
                        # but that would be an invalid input
                        prior = answer[i - 1]
                        if prior != ')':
                            # print(f'  Multiply {prior}')
                            changes = True
                            beforeElement = answer[:i - 1]
                            elementList = [prior]
                            elementCount = int(P)
                            elementDup = elementList * elementCount
                            afterCount = answer[i + 1:]
                            #print(f'{beforeElement}, {elementList}*{P}={elementDup}, {afterCount}')
                            # print(f'  {P} * {elementList}')
                            answer = beforeElement + elementDup + afterCount
                            break
                        elif prior == ')':
                            # print(f'  Multiply {lastOpenParenIndex} .. {i - 1}')
                            changes = True
                            beforeElement = answer[:lastOpenParenIndex]
                            elementList = answer[lastOpenParenIndex + 1:i - 1]
                            elementCount = int(P)
                            elementDup = elementList * elementCount
                            afterCount = answer[i + 1:]
                            #print(f'{beforeElement}, {elementList}*{P}={elementDup}, {afterCount}')
                            # print(f'  {P} * {elementList}')
                            answer = beforeElement + elementDup + afterCount
                            break
                if not changes:
                    break
                # print(f'{answer=}')
            return answer
        
        def flatAtomFormula(summed: Dict[str,int]) -> str:
            return ''.join([
                (
                    f'{element}{count}'
                    if count > 1
                    else element
                )
                for element, count in sorted(summed.items())
            ])
        
        parsed = parseAtomFormula(formula)
        # print(f'{parsed=}')

        multiplied = multiplyAtoms(parsed)
        # print(f'{multiplied=}')

        summed = Counter(multiplied)
        print(f'{summed=}')

        answer = flatAtomFormula(summed)
        return answer
# NOTE: works, but has Memory Limit Exceeded for large inputs
