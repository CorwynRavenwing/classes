class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        nums.sort()

        def canPickPPairsLETarget(target: int) -> bool:
            if target < 0:
                return False
            pairs = 0
            i = 0
            while pairs < p:
                # print(f'{i=}')
                if i + 1 >= len(nums):
                    # print(f'  ran out of array')
                    return False
                diff = nums[i + 1] - nums[i]
                if diff > target:
                    # print(f'  {diff=} too high')
                    i += 1
                    continue
                # print(f'  pick index {i} and {i+1}')
                pairs += 1
                i += 2
            # print(f'{p=} {pairs=}')
            return True

        L = -1  # b/c "0" is actually a legal answer sometimes
        left = canPickPPairsLETarget(L)
        if left:
            print(f'Strange, {L=} is true')
            return L
        R = max(nums) - min(nums)   # worst possible case
        right = canPickPPairsLETarget(R)
        if not right:
            print(f'Strange, {R=} is false')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = canPickPPairsLETarget(M)
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

# NOTE: Ignore hints, do it the "wrong" way, works perfectly :-/
# NOTE: Runtime 794 ms Beats 45.29%
# NOTE: Memory 30.67 MB Beats 95.07%

# NOTE: re-ran for challenge:
# NOTE: Runtime 462 ms Beats 24.69%
# NOTE: Memory 32.42 MB Beats 96.76%
