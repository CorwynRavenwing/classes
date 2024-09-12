class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:

        def minFlipsRow(row: List[int]) -> int:
            Len = len(row)
            Half = Len // 2
            firstHalf = row[:Half]
            lastHalf = row[Half:]
            lastRev = tuple(reversed(tuple(lastHalf)))
            differences = [
                1 if (A != B) else 0
                for (A, B) in zip(firstHalf, lastRev)
                # and throw away the center cell on odd-length rows
            ]
            return sum(differences)

        def minFlipsRowsOnly(grid: List[List[int]]) -> int:
            return sum([
                minFlipsRow(row)
                for row in grid
            ])
        
        return min([
            minFlipsRowsOnly(grid),
            minFlipsRowsOnly(zip(*grid))
        ])

# NOTE: Accepted on first Submit
# NOTE: Runtime 2666 ms Beats 5.01%
# NOTE: Memory 70.42 MB Beats 37.24%
