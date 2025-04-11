<pre>class Solution:
    def titleToNumber(self, columnTitle: str) -&gt; int:
        
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        values = [
            alphabet.index(letter)
            for letter in columnTitle
        ]
        print(f'{values=}')

        answer = 0
        for number in values:
            answer *= 26
            answer += number + 1

        return answer

# NOTE: Accepted on third Run (fencepost errors)
# NOTE: Accepted on first Submit
# NOTE: Runtime	0 ms Beats 100.00%
# NOTE: Memory 17.99 MB Beats 8.53%</pre>