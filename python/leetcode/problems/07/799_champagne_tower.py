class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        thisRow = (poured,)
        for rowNum in range(query_row):
            print(f'{thisRow}')
            nextRow = [0] * (len(thisRow) + 1)
            for i, val in enumerate(thisRow):
                val -= 1        # fills this glass
                if val <= 0:
                    continue    # no spillover
                val /= 2        # each gets half
                nextRow[i] += val
                nextRow[i + 1] += val
            thisRow = tuple(nextRow)
        
        print(f'{thisRow}')
        return min(1, thisRow[query_glass])

# NOTE: Accepted on first Submit
# NOTE: Runtime 135 ms Beats 11.37%
# NOTE: Memory 16.74 MB Beats 36.62%
