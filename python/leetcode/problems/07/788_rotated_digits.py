class Solution:

    # I know the question was for Good Numbers in the range [1..n],
    # and I am instead returning the range [0..n]; but since
    # 0 rotated is still 0, it's not a Good Number, and therefore
    # does not affect the count.  Starting the range at zero
    # makes the logic easier.

    def digitCount(self, n: int) -> int:
        return len(str(n))
    
    def splitDigits(self, n: int) -> int:
        strN = str(n)
        firstChar = strN[0]
        otherChars = strN[1:]
        return (int(firstChar), int(otherChars))
    
    def maxNumberOfNDigits(self, n: int) -> int:
        return (10 ** n) - 1
        # e.g. 3 digits -> 10^3 -> 1000 -> 999

    @cache
    def numbersContaining_0125689(self, n: int) -> int:
        DEBUG = False
        # these are numbers that can rotate, but may not be legal answers
        if DEBUG: print(f'numbersContaining_0125689({n}):')
        answer = 0
        digits = self.digitCount(n)
        if digits == 1:
            first_digit = n     # because it's only one digit
            for d in range(first_digit + 1):
                # d is every number LESS THAN OR EQUAL TO first_digit
                if d in [0, 1, 2, 5, 6, 8, 9]:
                    if DEBUG: print(f'  {n}:{d} +1')
                    answer += 1
                else:
                    if DEBUG: print(f'  {n}:{d} skip')
            return answer

        (first_digit, other_digits) = self.splitDigits(n)
        all_nines = self.maxNumberOfNDigits(digits - 1)
        for d in range(first_digit):
            # d is every number LOWER THAN first_digit
            if d in [0, 1, 2, 5, 6, 8, 9]:
                if DEBUG: print(f'  {n}:{d} +({all_nines})')
                answer += self.numbersContaining_0125689(all_nines)
            else:
                if DEBUG: print(f'  {n}:{d} skip {all_nines}')
        for d in {first_digit}:
            # d is EQUAL TO first_digit
            if d in [0, 1, 2, 5, 6, 8, 9]:
                if DEBUG: print(f'  {n}:{d} +({other_digits})')
                answer += self.numbersContaining_0125689(other_digits)
            else:
                if DEBUG: print(f'  {n}:{d} skip {other_digits}')
        return answer

    @cache
    def numbersContaining_2569(self, n: int) -> int:
        DEBUG = False
        # these are legal answers b/c they contain either 2, 5, 6, or 9
        if DEBUG: print(f'numbersContaining_2569({n}):')
        answer = 0
        digits = self.digitCount(n)
        if digits == 1:
            first_digit = n     # because it's only one digit
            for d in range(first_digit + 1):
            # d is every number LESS THAN OR EQUAL TO first_digit
                if d in [2, 5, 6, 9]:
                    if DEBUG: print(f'  {n}:{d} +1')
                    answer += 1
                else:
                    if DEBUG: print(f'  {n}:{d} skip')
            return answer
        (first_digit, other_digits) = self.splitDigits(n)
        all_nines = self.maxNumberOfNDigits(digits - 1)
        for d in range(first_digit):
            # d is every number LOWER THAN first_digit
            if d in [2, 5, 6, 9]:
                if DEBUG: print(f'  {n}:{d} +({all_nines})')
                answer += self.numbersContaining_0125689(all_nines)
            elif d in [0, 1, 8]:
                if DEBUG: print(f'  {n}:{d} +({all_nines})')
                answer += self.numbersContaining_2569(all_nines)
            else:
                if DEBUG: print(f'  {n}:{d} skip {all_nines}')
        for d in {first_digit}:
            # d is EQUAL TO first_digit
            if d in [2, 5, 6, 9]:
                if DEBUG: print(f'  {n}:{d} +({other_digits})')
                answer += self.numbersContaining_0125689(other_digits)
            elif d in [0, 1, 8]:
                if DEBUG: print(f'  {n}:{d} +({other_digits})')
                answer += self.numbersContaining_2569(other_digits)
            else:
                if DEBUG: print(f'  {n}:{d} skip {other_digits}')
        return answer

    def rotatedDigits(self, n: int) -> int:
        return self.numbersContaining_2569(n)

# NOTE: Accepted on first Submit
# NOTE: Runtime 39 ms Beats 94.35%
# NOTE: Memory 16.53 MB Beats 45.22%
# NOTE: and with cache:
# NOTE: Runtime 29 ms Beats 99.35%
# NOTE: Memory 17.06 MB Beats 9.13%
