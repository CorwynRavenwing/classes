class Solution:
    def maxValue(self, n: str, x: int) -> str:

        digits = list(n)
        xStr = str(x)
        answer = []
        if digits[0] == '-':
            # negative version: minimize magnitude
            answer.append(digits.pop(0))
            while True:
                P = None
                if digits:
                    P = digits.pop(0)
                    if P <= xStr:
                        print(f'{P=}')
                        answer.append(P)
                    else:
                        break
                else:
                    break
            answer.append(xStr)
            print(f'{xStr=}')
            if P is not None:
                print(f'{P=}')
                answer.append(P)
            print(f'... rest of digits (len={len(digits)})')
            answer.extend(digits)
        else:
            # positive version: maximixe magnitude
            while True:
                P = None
                if digits:
                    P = digits.pop(0)
                    if P >= xStr:
                        print(f'{P=}')
                        answer.append(P)
                    else:
                        break
                else:
                    break
            answer.append(xStr)
            print(f'{xStr=}')
            if P is not None:
                print(f'{P=}')
                answer.append(P)
            print(f'... rest of digits (len={len(digits)})')
            answer.extend(digits)

        return ''.join(answer)

