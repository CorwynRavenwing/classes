class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        
        # examine the grand total sum S:
        # case 1: it is odd.
        #   any pair of partitions adding to an odd number (S)
        #       must be one even and one odd.
        #   (even - odd) or (odd - even) is always odd.
        #   answer=zero.
        # case 2: it is even.
        #   any pair of partitions adding to an even number (S)
        #       must be both even or both odd.
        #   case 2a: both odd
        #       (odd - odd) is always even
        #   case 2b: both even
        #       (even - even) is always even
        #   therfore in both cases:
        #   answer=(number of possible partitions)
        #   answer=(length of nums) - 1

        # one-line version:
        return (len(nums) - 1) if (sum(nums) % 2 == 0) else 0

        # equivalent, readable version:
        S = sum(nums)
        if S % 2 == 0:
            return len(nums) - 1
        else:
            return 0

# NOTE: Acceptance Rate 75.0% (easy)

# NOTE: one-line answer, 23 lines of comments
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: O(1)
# NOTE: Memory 17.80 MB Beats 69.50%
# NOTE: O(1)
