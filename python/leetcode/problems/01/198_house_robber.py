class Solution:
    def rob(self, nums: List[int]) -> int:

        (just_robbed, just_skipped) = (0, 0)
        print(f'({just_robbed=}, {just_skipped=})')
        for this_house in nums:
            (just_robbed, just_skipped) = (
                just_skipped + this_house,
                max(just_robbed, just_skipped),
            )
            print(f'{this_house=}: ({just_robbed=}, {just_skipped=})')

        return max(just_robbed, just_skipped)

# NOTE: 30 ms; Beats 90.18% of users with Python3
