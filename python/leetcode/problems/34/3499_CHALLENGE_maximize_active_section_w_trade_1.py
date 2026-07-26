class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        
        original_ones = sum(map(int, s))
        print(f'{original_ones=}')

        zero_groups = tuple([
            i
            for i in map(len, s.split('1'))
            if i > 0
        ])
        print(f'{zero_groups=}')

        zero_additions = [
            (a + b)
            for (a, b) in pairwise(zero_groups)
        ]
        print(f'{zero_additions=}')

        max_zeros = max(zero_additions, default=0)
        print(f'{max_zeros=}')

        return max_zeros + original_ones

# NOTE: Acceptance Rate 34.3% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 623 ms Beats 72.90%
# NOTE: Memory 21.78 MB Beats 37.38%
