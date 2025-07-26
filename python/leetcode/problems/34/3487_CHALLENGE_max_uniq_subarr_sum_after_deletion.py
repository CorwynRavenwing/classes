class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        # make them unique
        nums = set(nums)
        print(f'{nums=}')

        max_nums = max(nums)
        if max_nums <= 0:
            print(f'Only choose the least bad value {max_nums}')
            return max_nums
        
        positive = [
            val
            for val in nums
            if val > 0
        ]
        print(f'{positive=}')
        print(f'Choose all positive values, once each')
        return sum(positive)

# NOTE: Acceptance Rate 31.2% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.71 MB Beats 51.76%
