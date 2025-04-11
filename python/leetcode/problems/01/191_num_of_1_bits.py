<pre>class Solution:
    def hammingWeight(self, n: int) -&gt; int:
        
        binary = f'{n:b}'
        print(f'{binary=}')
        bits = tuple(map(int, binary))
        print(f'{bits=}')
        return sum(bits)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 15.07%
# NOTE: Memory 18.07 MB Beats 11.11%</pre>