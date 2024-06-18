class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        if len(nums) == 1:
            print('only 1 value.  return it.')
            return nums[0]
        # now we can count on length >= 3 (an odd number)

        L = 0
        R = len(nums) - 1
        left = nums[L]
        right = nums[R]
        print(f'0 [{L},{R}] %[{L%2},{R%2}] =({left},{right})')
        check = nums[L+1]
        if left != check:
            print(f'found [{L}:{L+1}] <> ({left},{check})')
            return left
        else:
            print(f'L [{L}:{L+1}] = ({left},{check})')
        check = nums[R-1]
        if right != check:
            print(f'found [{R-1}:{R}] <> ({check},{right})')
            return right
        else:
            print(f'R [{R-1}:{R}] = ({check},{right})')
        R -= 1
        print(f'1 [{L},{R}] %[{L%2},{R%2}] =({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = nums[M]
            print(f'B [{L},{M},{R}] %[{L%2},{M%2},{R%2}] =({left},{mid},{right})')
            checkL = nums[M - 1]
            checkR = nums[M + 1]
            print(f'  check [{M-1}..{M+1}] %[{(M-1)%2}{M%2}{(M+1)%2}] =[{checkL},{mid},{checkR}]')
            if mid == checkL:
                print('  match left')
                M += 1
                mid = checkR    # which is nums[ old_M + 1 ]
            elif mid == checkR:
                print('  match right')
                # keep M
            else:
                print('  match neither side')
                return mid
            phase = M % 2
            print(f'phase {M=} %={phase}')
            if phase == 0:
                print('  replace left')
                (L, left) = (M, mid)
                continue
            if phase == 1:
                print('  replace right')
                (R, right) = (M, mid)
                continue
            raise Exception(f'{phase=} is neither 0 nor 1: should be impossible')

        check = nums[R+1]
        print(f'Z [{L},{R},{R+1}] %[{L%2}{R%2}{(R+1)%2}] =({left},{right},{check})')

        assert left != right
        assert right == check

        return left

