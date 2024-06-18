class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_1, value in enumerate(nums):
            print(f"#{index_1=} {value=}")
            remainder = target - value
            print(f"#  {remainder=}")
            try:
                index_2 = nums.index(remainder, index_1 + 1)
            except ValueError:
                continue
            return [index_1, index_2]

