class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

        nums.sort(
            key=lambda x: (abs(x), -x)
        )
        print(f'{nums=}')
        return nums.pop(0)

