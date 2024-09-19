class Solution:
    # @cache
    def allIndexes(self, haystack: str, needle: str) -> List[int]:
        answers = []
        pos = -1
        while True:
            try:
                pos = haystack.index(needle, pos + 1)
            except ValueError:
                break
            answers.append(pos)
        return answers

    # @cache
    def operatorIndexes(self, expression: str) -> List[int]:
        return tuple(sorted([
            index
            for op in ('+', '-', '*')
            for index in self.allIndexes(expression, op)
        ]))

    # @cache
    def diffWaysToCompute(self, expression: str) -> List[int]:
        print(f'DWTC({expression})')
        OI = self.operatorIndexes(expression)
        print(f'  {OI=}')
        
        if not OI:
            # no operators found: expression is a single number
            return [int(expression)]
        
        OPERATE = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
        }

        answers = []
        for index in OI:
            leftExpression = expression[:index]
            op = expression[index]
            rightExpression = expression[index + 1:]
            print(f'  ({leftExpression}) {op} ({rightExpression})')
            leftAnswers = self.diffWaysToCompute(leftExpression)
            print(f'  {leftExpression}: {leftAnswers=}')
            rightAnswers = self.diffWaysToCompute(rightExpression)
            print(f'  {rightExpression}: {rightAnswers=}')
            theseAnswers = [
                OPERATE[op](A, B)
                for A in leftAnswers
                for B in rightAnswers
            ]
            print(f'  A{op}B -> {theseAnswers=}')
            answers.extend(theseAnswers)
        return answers

# NOTE: Accepted on first Submit
# NOTE: Runtime 66 ms Beats 7.94%
# NOTE: Memory 16.87 MB Beats 8.08%
