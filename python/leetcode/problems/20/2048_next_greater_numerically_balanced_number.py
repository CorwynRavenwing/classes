class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        def differentAddititveFactors(d: int) -> List[List[int]]:
            # possible digits
            answers = set()
            possibles = {()}
            for i in range(1, 10):
                # print(f'{i=} {possibles=}')
                newPossibles = set()
                for P in possibles:
                    Q = P + (i,)
                    sumQ = sum(Q)
                    if sumQ == d:
                        # print(f'(answer {Q})')
                        answers.add(Q)
                        continue
                    elif sumQ > d:
                        # print(f'(too large: {sumQ}:{Q})')
                        continue
                    else:
                        newPossibles.add(Q)
                possibles |= newPossibles
            # print(f'done {possibles=}')
            return sorted(answers)

        def duplicate(factors: List[int]) -> List[int]:
            answer = []
            for F in factors:
                answer.extend([F] * F)
            return answer

        def buildNumberGreaterThan(n: int, digitList: List[int]) -> int:
            Nstr = str(n)
            queue = [('', Nstr, tuple(digitList))]
            while queue:
                Q = queue.pop(0)
                # print(f'{Q=}')
                (answerSoFar, Nstr, digitList) = Q
                if not Nstr and not digitList:
                    print(f'Attempt answer {answerSoFar}')
                    if len(answerSoFar) != len(str(n)):
                        print(f'  Error, wrong length.')
                        print(f'    {len(answerSoFar)=} != {len(str(n))=}')
                        continue
                    answer = int(answerSoFar)
                    if answer <= n:
                        print(f'  Error, too small')
                        print(f'    {answer=} <= {n=}')
                        continue
                    return answer
                if not Nstr or not digitList:
                    print(f'Error, {Nstr=} and {digitList=} should be the same length')
                    continue

                seen = set()
                for D in digitList:
                    if D in seen:
                        # print(f'  Already tried {D}')
                        continue
                    else:
                        seen.add(D)
                    strD = str(D)
                    newNstr = Nstr[1:]
                    if strD < Nstr[0]:
                        # print(f'  {D} too small ({Nstr[0]})')
                        continue
                    elif strD == Nstr[0]:
                        # print(f'  Equal {strD} == {Nstr[0]}')
                        newNstr = Nstr[1:]
                    elif strD > Nstr[0]:
                        # print(f'  bigger {strD} > {Nstr[0]}')
                        newNstr = '0' * (len(Nstr) - 1)
                    else:
                        raise Exception(f'error comparing {strD} <=> {Nstr[0]}')
                    newAnswer = answerSoFar + strD
                    newDigitList = list(digitList)
                    newDigitList.remove(D)
                    # print(f'  -> ({newAnswer}, {newNstr}, {tuple(newDigitList)})')
                    queue.append(
                        (newAnswer, newNstr, tuple(newDigitList))
                    )

        Nstr = str(n)
        digits = len(Nstr)
        print(f'Input {n=} has {digits} digits.')

        possibleSplits = differentAddititveFactors(digits)
        print(f'{possibleSplits=}')
        answers = []
        for Split in possibleSplits:
            digitList = duplicate(Split)
            print(f'{Split=} {digitList=}')
            answer = buildNumberGreaterThan(n, digitList)
            if answer is None:
                print(f'  cannot make a number > {n} from these digits')
                continue
            elif answer <= n:
                print(f'  returned number is not > {n}')
                continue
            else:
                print(f'  Found {answer}')
                answers.append(answer)
        if answers:
            return min(answers)
        
        newN = 10 ** digits     # BEFORE increasing 'digits'
        digits += 1
        print(f'Okay, trying {digits=} > {newN}')
        possibleSplits = differentAddititveFactors(digits)
        print(f'{possibleSplits=}')
        for Split in possibleSplits:
            digitList = duplicate(Split)
            print(f'{Split=} {digitList=}')
            answer = buildNumberGreaterThan(newN, digitList)
            if answer is None:
                print(f'  cannot make a number > {n} from these digits')
                continue
            elif answer <= n:
                print(f'  returned number is not > {n}')
                continue
            else:
                print(f'  Found {answer}')
                answers.append(answer)
        if answers:
            return min(answers)
# NOTE: Runtime 44 ms Beats 86.92%
# NOTE: Memory 16.73 MB Beats 14.62%
