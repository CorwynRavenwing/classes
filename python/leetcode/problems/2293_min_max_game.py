class Solution:
    def minMaxGame(self, nums: List[int]) -> int:

        while (n := len(nums)) > 1:
            print(f'{n=} {nums=}')
            newNums = list([
                (
                    min(nums[2 * i], nums[2 * i + 1])
                    if i % 2 == 0
                    else
                    max(nums[2 * i], nums[2 * i + 1])
                )
                for i in range(n // 2)
            ])
            nums = newNums
        print(f'{n=} {nums=}')
        return nums[0]

