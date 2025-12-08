class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        
        mod = 10 * 9 + 7

        # NOTE: DP(I) gives count of ways to partition the array
        # with the last partition ending at index I.
        # Therefore, DP(0) = 1, b/c max([A])-min([A])=0<=k.
        # DP(I) = sum(all DP(X) where X<I and [X..I] has a small enough difference)

        # Therefore we're going to need to do a Sliding Window for
        # min/max/diff, expanding the window right and setting DP(R) = the sum
        # of all the prior DP values between L and R-1.  If the diff is too big,
        # shrink the window from the left until it's okay, before doing this sum.
        # PartialSum can be a running total: as we expand right, we add the new
        # value to the sum; as we shrink left, we subtract DP(L) from the sum.

        # Do the Min/Max/Diff as a rolling calcuation as well.
        # A = nums[0]; Min=Max=A; Diff=0.  Values=[A].
        # as we expand right, B=nums[R]; bisort(Values, B).
        # If B>Max, Max=B; if B<Min, Min=B.
        # as we shrink left, A=nums[L]; delete(bisect(Values, A)).
        # If A==Max, Max=Values[-1]; if A==Min, Min=Values[0]

        answer = -99999

        return answer % mod

# NOTE: Acceptance Rate 40.0% (medium)
