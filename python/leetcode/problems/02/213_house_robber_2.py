class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        money = ((0,0), (0,0))
        # first pair: we robbed the first house; second pair we didn't
        # first of each pair: we just robbed the prior house; second we didn't

        print(f'{money=}')
        first_house = True
        for this_house in nums:
            if first_house:
                first_house = False
                money = (
                    (
                        this_house,  # robbed both first house and last-house-checked
                        0,
                    ),
                    (
                        0,
                        0,
                    )
                )
            else:
                # not first house
                robbed_first_and_prior = money[0][0]
                robbed_first_skipped_prior = money[0][1]
                robbed_prior = money[1][0]
                skipped_prior = money[1][1]
                money = (
                    (
                        robbed_first_skipped_prior + this_house,
                        max(robbed_first_and_prior, robbed_first_skipped_prior),
                    ),
                    (
                        skipped_prior + this_house,
                        max(robbed_prior, skipped_prior),
                    )
                )
            print(f'{this_house=}: {money=}')
        robbed_first_and_prior = money[0][0]
        robbed_first_skipped_prior = money[0][1]
        robbed_prior = money[1][0]
        skipped_prior = money[1][1]

        print(f'Invalid: {robbed_first_and_prior=}')

        return max([robbed_first_skipped_prior, robbed_prior, skipped_prior])

