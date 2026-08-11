class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        
        remaining = t
        allowed_factors = (2, 3, 5, 7)
        factors = []
        for F in allowed_factors:
            while (remaining % F) == 0:
                # print(F'{F=} {remaining}')
                factors.append(F)
                remaining //= F
        print(F'{factors=} {remaining=}')
        if remaining != 1:
            # not factorable into digits
            return "-1"

        def no_zero_digits(num: str) -> str:
            # should find any zeros,
            # make the first zero a 1,
            # make the rest of the digits all 1's
            pass
        
        # we would need to call this multiple times
        # with and without each possible set of
        # leftover digits.
        
        digits = list(map(int, num))
        REV = lambda L: tuple(reversed(L))
        digits_R = REV(digits)

        # print(f'{digits=}')
        # print(f'{digits_R=}')

        remaining = t
        allowed_digits = REV(range(1,10))
        digits_R = list(digits_R)
        answer_r = []

        print(f'0 {answer_r} : {digits_R}')
        for D in allowed_digits:
            while (remaining % D) == 0:
                if not digits_R:
                    print(f'  -> no digits_R')
                    break
                if remaining == 1:
                    print(f'  -> no remaining')
                    break
                current = digits_R.pop(0)
                answer_r.append(D)
                remaining //= D
                carry = (current > D)
                print(f'  {current} -> {D} {remaining=} {carry}')
                if carry:
                    if not digits_R:
                        digits_R.append(0)
                    digits_R[0] += 1
                print(f'1 {answer_r} : {digits_R}')

        print(f'2 {answer_r} : {digits_R}')
        while 0 in digits_R:
            current = digits_R.pop(0)
            D = 1
            answer_r.append(D)
            carry = (current > D)
            print(f'  {current} -> {D} {remaining=} {carry}')
            if carry:
                if not digits_R:
                    digits_R.append(0)
                digits_R[0] += 1
            print(f'3 {answer_r} : {digits_R}')

        answer_r.extend(digits_R)
        digits_R = []
        print(f'4 {answer_r} : {digits_R}')

        answer = REV(answer_r)
        answer = ''.join(map(str, answer))

        return answer

# NOTE: Acceptance Rate 19.1% (HARD)

# NOTE: Incomplete, need to execute the algorithm described
