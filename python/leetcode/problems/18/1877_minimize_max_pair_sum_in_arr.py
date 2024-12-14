class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # nums.sort()
        # max_sum = 0
        # while nums:
        #     A = nums.pop(-1)     # highest value
        #     B = nums.pop(0)      # lowest value
        #     Sum = A + B
        #     print(f'{A=} + {B=} = {Sum=}')
        #     max_sum = max(Sum, max_sum)
        # return max_sum

        nums.sort()
        return max(
            map(
                sum,
                zip(
                    nums,
                    reversed(nums)
                )
            )
        )

# NOTE: version 1 in file "-A": binary search; Time Limit Exceeded

# NOTE: version 2: .pop()
# NOTE: Accepted on second Run (variable-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 3731 ms Beats 5.16%
# NOTE: Memory 28.48 MB Beats 98.40%

# NOTE: version 3: built-in list functions
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 915 ms Beats 29.84%
# NOTE: Memory 31.16 MB Beats 6.69%

# NOTE: 4x faster runtime; half-again more memory
