class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def canReachTargetBalls(target: int) -> bool:
            if not target:
                # cannot split down to zero balls per bag
                return False
            
            opsLeft = maxOperations
            for N in nums:
                if N <= target:
                    continue

                # Should do div/mod math here instead, it would be faster:
                # while N > target:
                #     N -= target
                #     opsLeft -= 1
                #     if opsLeft < 0:
                #         return False
                
                # Yup, Time Limit Exceeded.  The faster way:
                Div, Mod = divmod(N, target)
                used_ops = Div - 1 + (0 if (Mod == 0) else 1)

                opsLeft -= used_ops
                if opsLeft < 0:
                    return False

            return True

        L = 0
        left = canReachTargetBalls(L)
        if left:
            print(f'Strange, {L=} is true')
            return L
        R = max(nums)
        right = canReachTargetBalls(R)
        if not right:
            print(f'Strange, {R=} is false')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = canReachTargetBalls(M)
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

# NOTE: version 1:
# NOTE: Accepted on first Run; Time Limit Exceeded on Submit
# NOTE: version 2:
# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 1279 ms Beats 6.84%
# NOTE: Memory 29.26 MB Beats 30.91%
