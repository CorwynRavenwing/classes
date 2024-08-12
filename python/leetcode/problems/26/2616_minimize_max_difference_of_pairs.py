class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        nums.sort()

    # this version is for minimizing something.

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



        return -99999




        # directly from Hint 3:
        def fn(i, x, depth=0):
            if (len(nums) - i) < (x * 2):
                # not enough numbers left
                # print(f'fn({i},{x}): not enough numbers left, ({len(nums)} - {i}) < ({x} * 2)')
                return None
            margin = '  ' * depth
            # print(f'fn({i},{x}):')
            # Hint had bug of missing base case when x=0
            if x <= 0:
                # print(f'  {x=} -> {0}')
                return 0
            # Hint had bug of missing base case when "i" runs out of array
            if i + 1 >= len(nums):
                # print(f'  {i}+1 too high')
                return None
            # print(f'{margin}fn({i},{x}):')
            nums_diff = abs(nums[i] - nums[i+1])
            # print(f'{margin}  {nums_diff} = abs([{i}]{nums[i]} - [{i+1}]{nums[i+1]}),')
            fn_i_plus_1_x = fn(i+1, x, depth + 1)
            # print(f'{margin}  fn({i+1},{x})={fn_i_plus_1_x}')
            fn_i_plus_2_x_minus_1 = fn(i+2, x-1, depth + 1)
            # ^ Hint had bug of "p" instead of "x"
            # print(f'{margin}  fn({i+2},{x-1})={fn_i_plus_2_x_minus_1}')
            max_section = (
                max(nums_diff, fn_i_plus_2_x_minus_1)
                if fn_i_plus_2_x_minus_1 is not None
                else None
            )
            # print(f'{margin}  {max_section=} = max({nums_diff}, {fn_i_plus_2_x_minus_1})')
            min_section = (
                min(fn_i_plus_1_x,max_section)   # Hint missing this close-paren
                if (fn_i_plus_1_x is not None) and (max_section is not None)
                else max_section
            )
            # print(f'{margin}  {min_section=} = min({fn_i_plus_1_x},{max_section})')

            return min_section

        return fn(0, p)
# NOTE: Ignore hints, do it the "wrong" way, works perfectly :-/
# NOTE: Runtime 794 ms Beats 45.29%
# NOTE: Memory 30.67 MB Beats 95.07%
