class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        DEBUG = False

        # we borrow some code from #1405:

        answer = 'X' * repeatLimit
        counts = Counter(s)
        while counts:
            found = False
            if DEBUG: print(f'{answer=}')
            MC = list(sorted(counts.items(), reverse=True))[:2]
            if len(MC) <= 1:
                MC.append(('X', 0))
            if DEBUG: print(f'{MC=}')

            ((letter1, num1), (letter2, num2)) = MC
            maxNum = repeatLimit
            if DEBUG: print(f'  "{letter1}" * {num1}/{maxNum}')
            if answer[-repeatLimit:] == (letter1 * repeatLimit):
                if DEBUG: print(f'    no: too many "{letter1}"')
                maxNum = 1
                letter1 = letter2
                num1 = num2
                if DEBUG: print(f'->"{letter1}" * {num1}/{maxNum}')

            if not num1:
                if DEBUG: print(f'  ran out of letters')
                break
            if num1 > maxNum:
                num1 = maxNum
            answer += (letter1 * num1)
            counts[letter1] -= num1
            found = True
            if not counts[letter1]:
                del counts[letter1]
                if DEBUG: print(f'    out of "{letter1}"')
        if DEBUG: print(f'{answer=}')
        answer = answer.replace('X', '')
        return answer

# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 697 ms Beats 9.42%
# NOTE: Memory 18.70 MB Beats 53.15%
