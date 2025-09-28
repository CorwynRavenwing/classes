class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        is_neg = False
        if numerator < 0:
            is_neg = not is_neg
            numerator = -numerator
        if denominator < 0:
            is_neg = not is_neg
            denominator = -denominator
        integer_part = numerator // denominator
        remain = numerator % denominator
        print(f'{numerator} / {denominator}: {integer_part} r{remain}')
        numerator -= integer_part * denominator
        remainders = {}
        decimal_part = []
        while remain and remain not in remainders:
            remainders[remain] = len(decimal_part)
            numerator *= 10
            next_digit = numerator // denominator
            remain = numerator % denominator
            print(f'{numerator} / {denominator}: {next_digit} r{remain}')
            numerator -= next_digit * denominator
            decimal_part.append(
                str(next_digit)
            )
        answer = '-' if is_neg else ''
        answer += str(integer_part)
        if decimal_part:
            repeating_part = []
            if remain:
                prior_index = remainders[remain]
                print(f'  found {prior_index=} for {remain=}')
                repeating_part = decimal_part[prior_index:]
                decimal_part = decimal_part[:prior_index]
            answer += '.' + ''.join(decimal_part)
            if repeating_part:
                answer += '(' + ''.join(repeating_part) + ')'
        if answer == "-0":
            answer = "0"
        return answer

# NOTE: Acceptance Rate 26.7% (medium)

# NOTE: re-ran for challenge:
# NOTE: Runtime 37 ms Beats 1.74%
# NOTE: Memory 18.25 MB Beats 20.31%
