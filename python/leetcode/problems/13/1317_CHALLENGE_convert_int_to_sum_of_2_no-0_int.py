class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        has_a_zero = lambda N: ('0' in str(N))

        no_zero = lambda N: (not has_a_zero(N))

        for A in range(n):
            B = n - A
            print(f'{A=} {B=}')
            if no_zero(A) and no_zero(B):
                return (A, B)

# NOTE: Acceptance Rate 58.0% (easy)

# NOTE: Accepted on first attempt
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.71 MB Beats 52.92%
