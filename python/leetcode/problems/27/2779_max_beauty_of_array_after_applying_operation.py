class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:

        nums.sort()
        answers = []
        i = 0
        j = 0
        while i <= j < len(nums):
            A = nums[i]
            B = nums[j]
            # print(f'[{i}..{j}] ({A},{B})')
            if B - A <= 2 * k:
                # print(f'  {B - A} ok: +J')
                answers.append(j - i + 1)
                j += 1
                continue
            else:
                # print(f'  {B - A} bad: -I')
                i += 1
                continue
        return max(answers)
# NOTE: Runtime 867 ms Beats 75.12%
# NOTE: Memory 30.64 MB Beats 35.21%
