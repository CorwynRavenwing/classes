class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        def canHitMaxOf(MAX: int) -> bool:
            # print(f'MAX({MAX}):')
            space = 0
            for N in nums:
                change = MAX - N    # pos if MAX>N, neg if MAX<N
                space += change
                # print(f'  {N}: {change=} {space=}')
                if space < 0:
                    # print(f'    NO')
                    return False
            # print(f'    YES')
            return True

        L = 0
        left = canHitMaxOf(L)
        if left:
            print(f'strange, left is True')
        R = max(nums)
        right = canHitMaxOf(R)
        if not right:
            print(f'strange, right is False')
        print(f'[{L},{R}] ({left},{right})')

        while L + 1 < R:
            M = (L + R) // 2
            med = canHitMaxOf(M)
            print(f'[{L},{M},{R}] ({left},{med},{right})')
            if med:
                print(f'yes: can go lower')
                (R, right) = (M, med)
                continue
            else:
                print(f'no: try going higher')
                (L, left) = (M, med)
                continue
        print(f'[{L},{R}] ({left},{right})')
        # R is now the lowest possible "yes" answer
        return R

