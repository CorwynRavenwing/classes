class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        def hashGrid(grid: List[List[int]]) -> Dict[List[int],int]:
            rowsHash = Counter(
                map(tuple, grid)
            )
            return rowsHash
        
        rowsHash = hashGrid(grid)
        print(f'{rowsHash=}')

        transposedGrid = tuple(zip(*grid))
        # print(f'{transposedGrid=}')

        colsHash = hashGrid(transposedGrid)
        print(f'{colsHash=}')

        hashSet = set(rowsHash) | set(colsHash)
        answer = 0
        for hash in hashSet:
            R = rowsHash[hash]
            C = colsHash[hash]
            print(f'{hash}: {R} * {C} = {R * C}')
            answer += R * C

        # print(f'{answer=}')
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 53 ms Beats 40.96%
# NOTE: Memory 22.73 MB Beats 5.33%
