class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        def flipRow(row: List[int]) -> List[int]:
            return tuple([(0 if val else 1) for val in row])
        
        def normalizeRow(row: List[int]) -> List[int]:
            return (flipRow(row) if row[0] else row)
        
        def cleanRow(row: List[int]) -> str:
            return ''.join(map(str, row))
        
        cleaned = tuple([
            cleanRow(normalizeRow(row))
            for row in matrix
        ])

        counted = Counter(cleaned)
        print(f'{counted=}')

        return max(counted.values())

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 85 ms Beats 28.26%
# NOTE: O(N*M)
# NOTE: Memory 19.98 MB Beats 17.11%
# NOTE: O(N)
# NOTE: re-ran later for challenge:
# NOTE: Runtime 91 ms Beats 25.93%
# NOTE: Memory 20.11 MB Beats 20.60%
