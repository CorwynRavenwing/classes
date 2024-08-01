class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:

        digits_In_First_Half = (intLength // 2) + (intLength % 2)
        # 6 -> 3 + 0; 5 -> 2 + 1 = 3.
        first_Number_With_D_digits = 10 ** (digits_In_First_Half - 1)   # 10^(2-1) = 10
        last_Number_With_D_digits = (10 ** digits_In_First_Half) - 1    # 10*2 - 1 = 99
        
        def make_palindrome(N: int, L: int) -> int:
            digits = list(str(N))
            rDigits = list(reversed(digits))
            if (len(digits) * 2) - 1 == L:
                rDigits = rDigits[1:]       # throw out the first digit
            answer = digits + rDigits
            if len(answer) != L:
                print(f'ERROR: {len(answer)=} != {L=}\n\t{answer=}')
                return -99
            return int(''.join(answer))

        def doQuery(N: int) -> int:
            Nth_number = first_Number_With_D_digits + N - 1
            if Nth_number > last_Number_With_D_digits:
                return -1

            return make_palindrome(Nth_number, intLength)
        
        return [
            doQuery(Q)
            for Q in queries
        ]

