class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        
        diffs = ''.join([
            (
                '+' if A < B else
                '=' if A == B else
                '-' if A > B else
                '?'
            )
            for (A, B) in pairwise(nums)
        ])
        print(f'Initial {diffs=}')

        if '=' in diffs:
            print(f'  equals: false')
            return False
        
        while '++' in diffs:
            diffs = diffs.replace('++', '+')
            print(f'  ++ {diffs=}')
        while '--' in diffs:
            diffs = diffs.replace('--', '-')
            print(f'  -- {diffs=}')
        
        print(f'Final {diffs=}')
        return (diffs == '+-+')

# NOTE: Acceptance Rate 48.5% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 1 ms Beats 89.47%
# NOTE: Memory 19.48 MB Beats 19.11%
