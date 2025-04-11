<pre>class Solution:
    def canWinNim(self, n: int) -&gt; bool:
        
        if n &lt; 4:
            # take all
            return True
        
        if n % 4 == 0:
            # whatever you take, he takes 4-N
            return False
        
        return True

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.82 MB Beats 34.75%</pre>