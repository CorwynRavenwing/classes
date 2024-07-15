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
        
        def parsedToCounted(parsed: List[str]) -> List[Tuple[str,int]]:
            answer = parsed
            for i, P in enumerate(answer):
                # print(f'::{i=} {P=}')
                if P in '()':
                    continue
                if P.isdigit():
                    continue
                P = Counter([P])
                answer[i] = P
            return answer

        def combineCounters(L: List[Counter]) -> Counter:
            # print(f'CC({L}):')
            answer = Counter()
            for C in L:
                # print(f' {C=}:')
                for element, count in C.items():
                    answer[element] += count
                    # print(f'    {element}+={count}')
            return answer

        def multiplyEachOfCounter(N: int, C: Counter) -> Counter:
            # print(f'XEC({N}, {C})')
            answer = Counter({
                element: N * count
                for element, count in C.items()
            })
            # print(f'-->{answer}')
            return answer

        def multiplyCounted(counted: List[Tuple[str,int]]) -> Counter:
            answer = []
            answer = parsed
            # print(f'{answer=}')
            while True:
                changes = False
                lastOpenParenIndex = None
                for i, P in enumerate(answer):
                    print(f'{i=} {P=}')
                    if P == '(':
                        lastOpenParenIndex = i
                        continue
                    if P == ')':
                        # print(f'  Merge {lastOpenParenIndex} .. {i - 1}')
                        changes = True
                        beforeOpenParen = answer[:lastOpenParenIndex]
                        elementList = answer[lastOpenParenIndex + 1:i]
                        elementMerge = combineCounters(elementList)
                        afterCloseParen = answer[i + 1:]
                        #print(f'{beforeOpenParen}, {elementList} -> {elementMerge}', {afterCloseParen}')
                        print(f'{elementList} -> {elementMerge}')
                        # print(f'  {P} * {elementList}')
                        answer = beforeOpenParen + [elementMerge] + afterCloseParen
                        break
                    if str(P).isdigit():
                        # following line will fail if a number is the first object
                        # but that would be an invalid input
                        prior = answer[i - 1]
                        # print(f'  Multiply {prior}')
                        changes = True
                        beforeElement = answer[:i - 1]
                        element = prior
                        elementCount = int(P)
                        elementDup = multiplyEachOfCounter(elementCount, element)
                        afterCount = answer[i + 1:]
                        #print(f'{beforeElement}, {element}*{P}={elementDup}, {afterCount}')
                        # print(f'  {P} * {element}')
                        answer = beforeElement + [elementDup] + afterCount
                        break
                if not changes:
                    break
                # print(f'{answer=}')
            return combineCounters(answer)
        
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
        print(f'{parsed=}')

        counted = parsedToCounted(parsed)
        print(f'{counted=}')

        multiplied = multiplyCounted(counted)
        print(f'{multiplied=}')

        summed = multiplied
        # summed = Counter(multiplied)
        # print(f'{summed=}')

        answer = flatAtomFormula(summed)
        return answer

