class Solution:
    def superPow(self, a: int, b: List[int]) -> int:

        # shortcuts:
        # (a ^ b) mod X === ((a mod X) ^ b) mod X
        # a ^ (b + c) === (a ^ b) * (a ^ c)
        # a ^ (bc) === (a ^ b) ^ c

        # therefore, a ^ B=[X, Y, Z]
        # == a ^ ((X * 100) + (Y * 10) + Z)
        # == a ^ ((((X)*10 + Y) * 10) + Z)
        # == (a ^ ((((X)*10 + Y) * 10)) * (a ^ Z)
        # == ((a ^ ((((X)*10 + Y)) ^ 10) * (a ^ Z)
        # == ((a ^ ((X)*10)) * (a ^ Y))) ^ 10) * (a ^ Z)
        # == (((a ^ X) ^ 10) * (a ^ Y)) ^ 10) * (a ^ Z)
        # so, start at head of B,
        # accumulator = a^head
        # if next_value,
        #   take accumulator ^ 10 times a ^ next_value
        # which (since 1 ^ 10 == 1), is equivalent to:

        mod = 1337
        accumulator = 1
        print(f'start={accumulator}')
        for b_digit in b:
            accumulator **= 10
            accumulator %= mod
            print(f'^10={accumulator}')
            accumulator *= (a ** b_digit)
            accumulator %= mod
            print(f'*a^{b_digit}={accumulator}')
        return accumulator

