<pre>class Solution:
    def getRow(self, rowIndex: int) -&gt; List[int]:
        
        # we borrow some code from #118:
        row = []
        for i in range(rowIndex + 1):
            if row == []:
                row = [1]
            else:
                prev_row = [0] + row + [0]
                row = []
                for A, B in pairwise(prev_row):
                    row.append(A + B)

        return row

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.96 MB Beats 11.80%</pre>