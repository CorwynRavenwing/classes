class Solution:
    def maxProduct(self, n: int) -> int:
        
        # NOTE: "max product of 2 digits"
        # === "product of max 2 digits"

        digits = tuple(sorted(map(int, str(n))))
        print(f'{digits=}')

        (A, B) = digits[-2:]
        print(f'{A=} {B=}')

        return A * B

# NOTE: Acceptance Rate 69.5% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.22 MB Beats 54.97%
