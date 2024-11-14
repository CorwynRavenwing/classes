class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        # SHORTCUT: any time I hear "minimize the maximum of ..." I always
        # jump immediately to Binary Search.
        # ... checks Hints: yes, that's what they recommend as well.

        def canFitWithTargetMaximum(target: int) -> bool:
            if target == 0:
                return False
            count = 0
            for Q in quantities:
                # print(f'  DEBUG: {Q=}')
                (quotient, remainder) = divmod(Q, target)
                # print(f'  DEBUG: (Q,R)={(quotient,remainder)}')
                count += quotient
                if remainder > 0:
                    count += 1
                # print(f'  DEBUG: {count=}')
                if count > n:
                    # print(f'    NO')
                    return False

            # print(f'    YES')
            return True

        L = 0
        left = canFitWithTargetMaximum(L)
        if left:
            print(f'Strange, {L=} is true')
            return L
        R = max(quantities)
        right = canFitWithTargetMaximum(R)
        if not right:
            print(f'Strange, {R=} is false')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = canFitWithTargetMaximum(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Right')
                (R, right) = (M, mid)
            else:
                print(f'  False: replace Left')
                (L, left) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # R is now the lowest possible True value
        return R

# NOTE: Accepted on second Run (first was variable-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 998 ms Beats 27.66%
# NOTE: Memory 28.87 MB Beats 50.11%
