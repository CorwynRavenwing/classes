class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        
        # we borrow some code from #3349:

        changes = ''.join([
            (
                '+' if A < B else '-'
            )
            for (A, B) in pairwise(nums)
        ])
        # print(f'{changes=}')

        def isPossible(k: int) -> bool:
            # Here, True is good and happens for lower numbers
            print(f'isPossible({k}):')
            plus = '+' * (k - 1)
            # print(f'  {plus=}')

            for joiner in '-+':
                print(f'  "{joiner}"')
                pattern = f'{plus}{joiner}{plus}'
                # print(f'  {pattern=}')
                if pattern in changes:
                    print(f'    YES')
                    return True

            print(f'  NO')
            return False

        # this version is for maximizing something.

        nums.sort()

        L = 0
        left = isPossible(L)
        if not left:
            print(f'Strange, {L=} is false')
            return L
        R = len(nums) + 1
        right = isPossible(R)
        if right:
            print(f'Strange, {R=} is true')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = isPossible(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Left')
                (L, left) = (M, mid)
            else:
                print(f'  False: replace Right')
                (R, right) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # L is now the highest possible True value
        return L

# NOTE: Acceptance Rate 45.6% (medium)

# NOTE: Accepted on second Run (variable capitalization typo)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 1437 ms Beats 49.03%
# NOTE: Memory 45.84 MB Beats 39.35%
