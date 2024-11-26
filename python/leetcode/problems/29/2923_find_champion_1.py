class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        
        rowSums = tuple(map(sum, grid))
        print(f'{rowSums=}')

        for team, count in enumerate(rowSums):
            if count + 1 == len(grid):
                return team

        return -1

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 11 ms Beats 22.92%
# NOTE: Memory 17.30 MB Beats 37.65%
