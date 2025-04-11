<pre>class Solution:
    def generate(self, numRows: int) -&gt; List[List[int]]:
        
        answer = []
        row = []
        for i in range(numRows):
            if row == []:
                row = [1]
            else:
                prev_row = [0] + row + [0]
                row = []
                for A, B in pairwise(prev_row):
                    row.append(A + B)
            answer.append(row)

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.87 MB Beats 37.42%</pre>