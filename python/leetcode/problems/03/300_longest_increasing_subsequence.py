class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

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
        
        return max(data)

# NOTE: Runtime 1155 ms Beats 68.86%
# NOTE: Memory 17.16 MB Beats 11.06%
