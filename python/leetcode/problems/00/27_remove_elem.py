<pre>class Solution:
    def removeElement(self, nums: List[int], val: int) -&gt; int:
        
        while val in nums:
            nums.remove(val)
        return len(nums)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.90 MB Beats 11.34%</pre>