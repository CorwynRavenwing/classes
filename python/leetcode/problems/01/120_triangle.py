class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        INF = [float('+inf')]
        pathSums = []
        for row in triangle:
            print(f'ROW: {row}')
            if not pathSums:
                pathSums = row
                continue
            priorPathSums = INF + pathSums + INF
            # print(f'PRI: {priorPathSums}')
            minPathSums = [min(A,B) for (A,B) in pairwise(priorPathSums)]
            print(f'MIN: {minPathSums}')
            pathSums = [A + B for (A,B) in zip(row, minPathSums)]
            print(f'SUM: {pathSums}')

        return min(pathSums)

# NOTE: Accepted on first Submit
# NOTE: Runtime 58 ms Beats 77.77%
# NOTE: Memory 17.64 MB Beats 63.87%
