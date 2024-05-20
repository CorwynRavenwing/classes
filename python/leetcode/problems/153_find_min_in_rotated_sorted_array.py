class Solution:
    def findMin(self, nums: List[int]) -> int:

        first = nums[0]
        L = 0
        R = len(nums) - 1
        left = nums[L]
        right = nums[R]
        print(f'0 [{L},{R}] = ({left},{right}) {first=}')
        if right > left:
            print('still sorted')
            return left
        if L == R:
            print('one element')
            return left
        while L + 1 < R:
            M = (L + R) // 2
            mid = nums[M]
            print(f'B [{L},{M},{R}] = ({left},{mid},{right}) {first=}')
            if mid > first:
                print('  replace left')
                (L, left) = (M, mid)
                continue
            if mid < first:
                print('  replace right')
                (R, right) = (M, mid)
                continue
            raise Exception(f'{mid=} neither < nor > {first=}')
        print(f'Z [{L},{R}] = ({left},{right}) {first=}')
        if right < first:
            print(f'found {right=}')
            return right
        if left < first:
            raise Exception(f'{left=} should not be < {first=} here')
        raise Exception(f'should not get here ({left=},{right=})')

