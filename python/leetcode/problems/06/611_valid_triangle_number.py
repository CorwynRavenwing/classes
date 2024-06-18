class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort()
        print(f'{nums=}')
        retval = 0
        for i, A in enumerate(nums):
            if A == 0:
                continue
            # print(f'[{i}] {A=}')
            for j, B in enumerate(nums):
                if i >= j:
                    continue
                # print(f'  [{j}] {B=}')
                L = j + 1
                if L >= len(nums):
                    # print(f'  no numbers left {L=} {len(nums)=}')
                    continue
                R = bisect.bisect_left(nums, A + B, L)
                all_C = R - L
                # print(f'    +{all_C} {A}+{B}={A+B} nums[{L}:{R}]={nums[L:R]}')
                retval += all_C
                continue

        return retval

