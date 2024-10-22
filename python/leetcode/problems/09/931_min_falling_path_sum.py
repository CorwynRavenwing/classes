class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        # PROCESS: for each row, we add the value at that location
        # to the minimum of the three higher values that could
        # fall through this cell.
        
        def PairwiseMin(row: List[int]) -> List[int]:
            return tuple(
                map(
                    min,
                    pairwise(
                        tuple(row)
                    )
                )
            )

        def ThreewiseMin(row: List[int]) -> List[int]:
            INF = float('+inf')
            pass1 = (INF,) + tuple(row) + (INF,)
            pass2 = PairwiseMin(pass1)
            pass3 = PairwiseMin(pass2)
            return pass3
        
        priorValues = matrix[0]
        for i in range(1, len(matrix)):
            row = matrix[i]
            priorMin = ThreewiseMin(priorValues)
            currentValues = tuple(
                map(
                    sum,
                    zip(row, priorMin)
                )
            )
            priorValues = currentValues
        
        return min(priorValues)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 23 ms Beats 98.52%
# NOTE: Memory 17.40 MB Beats 77.48%
