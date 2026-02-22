class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        # NOTE: since left and right are <= 10^6,
        # and 10^6 (1000000) is < 2^20 (1048576),
        # we can use this minimal prime-checker:

        def is_small_prime(i: int) -> bool:
            small_primes = [2, 3, 5, 7, 11, 13, 17, 19]
            return i in small_primes
        
        def set_bits(i: int) -> int:
            binary = f'{i:b}'
            digits = tuple(map(int, binary))
            return sum(digits)

        answers = [
            (
                1
                if is_small_prime(set_bits(i))
                else
                0
            )
            for i in range(left, right + 1)
        ]

        print(f'{answers=}')

        return sum(answers)

# NOTE: Acceptance Rate 72.6% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 623 ms Beats 11.99%
# NOTE: Memory 19.28 MB Beats 76.40%
