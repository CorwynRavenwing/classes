<pre>class Solution:
    def minOperations(self, nums: List[int], k: int) -&gt; int:
        
        # SHORTCUT: we don't care about how many of each value
        # there are, only about how many different values/

        nums = set(nums)

        # SHORTCUT: our operation cannot make numbers larger.
        # If the minimum number is too low, it's impossible.

        min_num = min(nums)
        if min_num &lt; k:
            return -1
        elif min_num == k:
            return len(nums) - 1
        else:
            return len(nums)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 71 ms Beats 29.72%
# NOTE: Memory 17.83 MB Beats 35.61%</pre>