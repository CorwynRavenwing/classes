class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # NOTE: the max value of ((nums[i]-1) * (nums[j]-1))
        # === (max 2 values in array) (-1) (multiplied)

        nums.sort()
        (A, B) = nums[-2:]
        print(f'{A=} {B=}')

        return (A-1) * (B-1)

# NOTE: Acceptance Rate 83.6% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.22 MB Beats 68.04%
