class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        
        topline = '.' * n
        others = '#' * (n-1) + '.'
        return (
            (topline,)
            +
            (others,) * (m-1)
        )

# NOTE: Acceptance Rate 76.5%

# NOTE: effectively a one-liner
# NOTE: Accepted on second Run (confusion between (x) parens vs (x,) tuples)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.23 MB Beats 62.30%
