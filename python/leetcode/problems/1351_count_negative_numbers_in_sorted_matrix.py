class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        negatives = [
            N
            for row in grid
            for N in row
            if N < 0
        ]
        return len(negatives)
        
        # "95 ms.  Beats 92.55% of users with Python3".
        # Does not need binary-search optimization.

