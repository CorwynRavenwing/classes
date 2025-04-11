<pre>class Solution:
    def reverseBits(self, n: int) -&gt; int:
        
        binary = f'{n:032b}'
        print(f'{binary=}')
        yranib = ''.join(reversed(binary))
        print(f'{yranib=}')

        return int(yranib, 2)

        return -99999

# NOTE: Accepted on second Run (vague problem definition, &quot;reverse&quot; vs 
&quot;invert&quot;)
# NOTE: Accepted on first Submit
# NOTE: Runtime 35 ms Beats 83.02%
# NOTE: Memory 18.00 MB Beats 15.22%</pre>