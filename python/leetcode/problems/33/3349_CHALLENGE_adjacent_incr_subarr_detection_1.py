class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        
        changes = ''.join([
            (
                '+' if A < B else '-'
            )
            for (A, B) in pairwise(nums)
        ])
        print(f'{changes=}')

        plus = '+' * (k - 1)
        print(f'{plus=}')
        
        for joiner in '-+':
            pattern = f'{plus}{joiner}{plus}'
            print(f'{pattern=}')
            if pattern in changes:
                print(f'  YES')
                return True

        print(f'NO')
        return False

# NOTE: Acceptance Rate 45.1% (easy)

# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 89 ms Beats 36.90%
# NOTE: Memory 17.80 MB Beats 64.71%
