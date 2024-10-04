class Solution:
    def minMoves(self, nums: List[int]) -> int:

        # SHORTCUT: "increment n-1 out of n elements"
        # === "decrement 1 element"
        # === "amount by which all the other numbers exceed min()"
        # === "sum() - len() * min()"

        return sum(nums) - len(nums) * min(nums)

# NOTE: Yes, four lines of comments for a one-line answer
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: By eye, it's O(N) time and O(1) space
# NOTE: Runtime 192 ms Beats 83.29%
# NOTE: Memory 18.12 MB Beats 20.08%
