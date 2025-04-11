<pre>class Solution:
    def missingNumber(self, nums: List[int]) -&gt; int:
        values = set(range(len(nums) + 1)) - set(nums)
        return values.pop()

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 4 ms Beats 49.05%
# NOTE: Memory 19.79 MB Beats 6.44%</pre>