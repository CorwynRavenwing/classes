class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        counts = Counter(nums)
        nums.sort(
            key=lambda x: (counts[x], -x)
        )
        return nums
# NOTE: Runtime 51 ms Beats 49.72% (a while ago)
# NOTE: Runtime 54 ms Beats 26.71%
# NOTE: Memory 16.60 MB Beats 59.57%

