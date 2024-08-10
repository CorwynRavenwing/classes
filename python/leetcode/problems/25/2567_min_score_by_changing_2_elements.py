class Solution:
    def minimizeSum(self, nums: List[int]) -> int:

        # SHORTCUT: we are change two numbers, so we can always
        # move one or both of them to being the same as another
        # number that we're not moving.
        # Therefore the low score will always be *zero*
        
        # SHORTCUT: since we're moving a number to being the same
        # as something else, that's equivalent to deleting it.

        # Our reasonable choices for each of the two turns
        # is either the current minimum or maximum, whichever
        # does us more good.  We have two such turns.  Therefore our
        # possible resultant lists, for a list [A, B, C, ... X, Y, Z], are:
        # [A, B, C, ... X]
        # [B, C, ... X, Y]  # this can be reached two ways
        # [C, ... X, Y, Z]
        # and our answers are therefore (X-A), (Y-B), and (Z-C), whichever is lowest.

        if len(nums) <= 3:
            # move any 2 to make them all the same
            return 0
        
        nums.sort()
        return min([
            nums[-3] - nums[0],
            nums[-2] - nums[1],
            nums[-1] - nums[2],
        ])
# NOTE: Runtime 270 ms Beats 47.33%
# NOTE: Memory 29.23 MB Beats 9.33%
