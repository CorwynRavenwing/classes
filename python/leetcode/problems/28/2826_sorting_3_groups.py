class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        countsByIndex = {
            value: (0,) + tuple(
                accumulate([
                    (1 if N == value else 0)
                    for N in nums
                ])
            )
            for value in [1, 2, 3]
        }
        print(f'{countsByIndex=}')
        N = len(nums)
        changes = [
            (
                (i - 0) - (countsByIndex[1][i] - countsByIndex[1][0])
            ) + (
                (j - i) - (countsByIndex[2][j] - countsByIndex[2][i])
            ) + (
                (N - j) - (countsByIndex[3][N] - countsByIndex[3][j])
            )
            for i in range(0, N + 1)
            for j in range(i, N + 1)
        ]
        print(f'{changes=}')
        
        return min(changes)
# NOTE: Runtime 487 ms Beats 5.03%
# NOTE: Memory 17.59 MB Beats 6.53%
