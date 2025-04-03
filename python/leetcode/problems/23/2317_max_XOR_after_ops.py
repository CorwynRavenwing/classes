class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        
        # SHORTCUT 1: the operation is able to clear any bit
        # or set of bits in each element of nums.

        # SHORTCUT 2: to maximize the grand total XOR value,
        # clear each available bit all but one (or any odd
        # number) of times.

        # SHORTCUT 3: the grand total XOR value will then
        # be exactly the grand total (non-exclusive) OR value
        # of the original nums array.

        return reduce(operator.or_, nums)
        # yes, 1 line of code with 15 lines of comments :-)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 6 ms Beats 78.57%
# NOTE: Memory 27.55 MB Beats 10.71%
