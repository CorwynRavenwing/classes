class Solution:

    # we borrow some code from #300:

    def lengthOfLISbyIndex(self, nums: List[int]) -> List[int]:

        # data[i] = length of best sequence ending at position i
        data = [None] * len(nums)

        i = 0
        # print(f'{i=} {data[:i]=}\n')

        for i in range(0, len(nums)):
            # print(f'{i=} {data[:i]=}')
            # print(f'  {nums[:i]=} {nums[i]=}')
            priors = [
                Dval
                for Dindex, Dval in enumerate(data[:i])
                if nums[Dindex] < nums[i]
            ]
            # print(f'    {priors=}')
            best_prior = (
                max(priors)
                if priors
                else 0
            )
            data[i] = best_prior + 1
            # print(f'    {best_prior=} {data[i]=}')

        return data

    def minimumMountainRemovals(self, nums: List[int]) -> int:

        REV = lambda x: tuple(reversed(tuple(x)))

        increases = self.lengthOfLISbyIndex(nums)
        decreases = REV(self.lengthOfLISbyIndex(REV(nums)))
        print(f'{increases=}')
        print(f'{decreases=}')

        mountains = [
            (
                (INC + DEC - 1)             # -1 b/c center peak is counted twice
                if (INC > 1) and (DEC > 1)  # so that there is both and up and down
                else -1
            )
            for (INC, DEC) in zip (increases, decreases)
        ]
        print(f'{mountains=}')

        max_mountain_length = max(mountains)

        return len(nums) - max_mountain_length

# NOTE: Acceptance Rate 51.6% (HARD)
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 1175 ms Beats 66.04%
# NOTE: Memory 17.08 MB Beats 6.79%
