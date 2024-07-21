class Solution:
    def countGoodNumbers(self, n: int) -> int:

        mod = 10 ** 9 + 7

        def power_mod(base: int, power: int) -> int:
            print(f'power_mod({base},{power}):')
            if power > 10:
                # A^((B*C) + D) == A^(B*C) * A^D == (A^B)^C * A^D
                A = base
                B = 10
                C = power // 10
                D = power % 10
                print(f'  {A=} {B=} {C=} {D=}')
                AtoB = power_mod(A, B)
                AtoBC = power_mod(AtoB, C)
                AtoD = power_mod(A, D)
                answer = AtoBC * AtoD
                print(f'  A^B={AtoB}, ^C={AtoBC}, A^D={AtoD}')
                return answer % mod
            else:
                print(f'  simple')
                return (base ** power) % mod

        even_string = '24680'
        odd_string = '2357'
        even_choices = len(even_string)
        odd_choices = len(odd_string)

        # e.g. n=5: 'EoEoE', n//2 is 2 which is the odd digits;
        # 5 being odd (n%2==1), the even digits need one more.
        # for n=4, 'EoEo', n//2 is also 2 which is the right answer for both.
        even_digits = (n // 2) + (n % 2 == 1)
        odd_digits = (n // 2)
        print(f'{n=} {even_digits=} {odd_digits=}')

        print(f'good_numbers\n  = even ({even_choices} ** {even_digits})')
        print(f'  * odd ({odd_choices} ** {odd_digits})')
        good_numbers = power_mod(even_choices, even_digits) * power_mod(odd_choices, odd_digits)

        return good_numbers % mod

