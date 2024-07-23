class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        counts = Counter(nums)
        nums.sort(
            key=lambda x: (counts[x], -x)
        )
        return nums
# NOTE: Runtime 51 ms Beats 49.72%
