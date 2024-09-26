class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counts = Counter(nums)
        most_common_tuples = counts.most_common(1)
        (value, count) = most_common_tuples[0]
        if count >= len(nums) // 2:
            return value
        else:
            raise ValueError(f'No Majority Element: {value=} {count=} {len(nums)=}')

# NOTE: Accepted on first Submit
# NOTE: Runtime 166 ms Beats 77.72%
# NOTE: Memory 18.12 MB Beats 23.47%
