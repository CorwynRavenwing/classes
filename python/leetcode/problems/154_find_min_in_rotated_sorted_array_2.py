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
        if left == right:
            print(f'{left=} == {right=}')
            # first few, and last few, elements are the same.
            # CANNOT TELL [10 1 10 10 10] from [10 10 10 1 10] with binary search!
            # therefore remove all the 10's, but remember them as a possible answer
            while (L < len(nums) - 1) and (nums[L] == left):
                L += 1
            while (R > 0) and (nums[R] == left):
                R -= 1
            if L > R:
                print(f'{L=} > {R=}: it is all one number')
                return left
            print(f'recursive search in nums[{L}:{R+1}]={nums[L:R+1]}')
            answer = self.findMin(nums[L:R+1])
            print(f'found {answer=} (compare {first})')
            return min(answer, first)

        while L + 1 < R:
            M = (L + R) // 2
            mid = nums[M]
            print(f'B [{L},{M},{R}] = ({left},{mid},{right}) {first=}')
            if mid >= first:
                print('  replace left')
                (L, left) = (M, mid)
                continue
            if mid < first:
                print('  replace right')
                (R, right) = (M, mid)
                continue
            raise Exception(f'{mid=} neither <, ==, > {first=}')
        print(f'Z [{L},{R}] = ({left},{right}) {first=}')
        if right <= first:
            print(f'found {right=}')
            return right
        if left < first:
            raise Exception(f'{left=} should not be < {first=} here')
        raise Exception(f'should not get here ({left=},{right=})')

