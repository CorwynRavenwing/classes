class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        
        i = len(nums) - 2   # two from the end
        while i >= 0:
            # print(f'{nums=}')
            (A, B) = nums[i:i+2]
            # print(f'{i}: {A} {B}')
            if A > B:
                # print(f'  Last number too small: delete')
                # (B can't be the answer b/c it's smaller than A)
                nums[i+1] = None
                i -= 1
                continue
            else:
                # print(f'  Combine last two into {A+B}')
                nums[i] = A + B
                nums[i + 1] = None
                i -= 1
                continue
        # print(f'{nums=}')

        return nums[0]
# NOTE: Runtime 746 ms Beats 27.59%
# NOTE: Memory 27.87 MB Beats 84.48%
