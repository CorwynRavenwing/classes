class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        return len([
            N
            for N in range(1,1001)
            if a % N == 0 and b % N == 0
        ])
        # one-line answer

# NOTE: Acceptance Rate 80.5% (easy)

# NOTE: Accepted on second Run (div zero error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.28 MB Beats 55.69%
