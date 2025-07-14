class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        
        maxes = tuple(accumulate(nums, max))
        print(f'{maxes=}')

        conver = tuple(map(sum, zip(nums, maxes)))
        print(f'{conver=}')

        scores = tuple(accumulate(conver))
        print(f'{scores=}')

        return scores

# NOTE: Acceptance Rate 72.0% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 110 ms Beats 6.08%
# NOTE: Memory 45.56 MB Beats 8.84%
