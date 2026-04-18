class Solution:
    def mirrorDistance(self, n: int) -> int:

        def reverse_int(N: int) -> int:
            N_str = f'{N}'
            reverse_str = ''.join(reversed(N_str))
            reverse_N = int(reverse_str)
            print(f'{N} -> {reverse_N}')
            return reverse_N
        
        rev_n = reverse_int(n)
        return abs(n - rev_n)

# NOTE: Acceptance Rate 87.8% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.18 MB Beats 86.%
