class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        def triangulate(nums: List[int]) -> List[int]:
            if len(nums) == 1:
                return nums
            
            MOD10 = lambda N: (N % 10)
            
            nums = tuple(
                map(
                    MOD10,
                    map(
                        sum,
                        pairwise(nums)
                    )
                )
            )
            return nums
        
        # print(f'{nums}')
        while len(nums) > 1:
            nums = triangulate(nums)
            # print(f'{nums}')
        
        return nums[0]

# NOTE: Acceptance Rate 79.8% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 2442 ms Beats 5.06%
# NOTE: Memory 18.70 MB Beats 13.05%

# NOTE: re-ran for challenge:
# NOTE: Runtime 2421 ms Beats 5.07%
# NOTE: Memory 18.54 MB Beats 16.05%
