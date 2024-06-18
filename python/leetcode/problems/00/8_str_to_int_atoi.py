class Solution:
    def myAtoi(self, s: str) -> int:

        def atoi_digit(char: str) -> int:
            if len(char) == 1 and '0' <= char <= '9':
                return ord(char) - ord('0')

        print(f'0: "{s}"')
        s = s.strip()
        print(f'1: "{s}"')
        if len(s) == 0:
            print(f'3: zero-length string')
            return 0
        first = s[0]
        if first == '-':
            s = s[1:]
            is_neg = True
        elif first == '+':
            s = s[1:]
            is_neg = False
        else:
            # don't trim off first character
            is_neg = False
        print(f'2: {is_neg=} "{s}"')
        s = s.lstrip('0')
        print(f'3a: "{s}"')
        T = []
        for char in s:
            if char.isdigit():
                T.append(char)
            else:
                print(f'  non-digit "{char}": stop')
                break
        s = ''.join(T)
        print(f'3b: {s}')
        # -(2**31)=-2147483648 2**31-1=2147483647
        if len(s) > len('2147483648'):
            print(f'4. number longer than MAXINT ...')
            if is_neg:
                print(f'4. returning -MAXINT')
                return -2147483648
            else:
                print(f'4. returning +MAXINT')
                return 2147483647
        if len(T) == len('2147483648'):
            print(f'4. number as long as MAXINT ...')
            if is_neg and s >= '2147483648':
                print(f'4. returning -MAXINT')
                return -2147483648
            if not is_neg and s >= '2147483647':
                print(f'4. returning +MAXINT')
                return 2147483647
        answer = 0
        for char in s:
            answer *= 10
            answer += atoi_digit(char)
        print(f'3c: {is_neg=} {answer}')
        if is_neg:
            answer *= -1
        return answer

