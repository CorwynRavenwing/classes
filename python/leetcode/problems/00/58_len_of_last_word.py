<pre>class Solution:
    def lengthOfLastWord(self, s: str) -&gt; int:
        
        words = s.split(' ')
        while '' in words:
            words.remove('')
        last = words[-1]
        return len(last)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.76 MB Beats 61.15%</pre>