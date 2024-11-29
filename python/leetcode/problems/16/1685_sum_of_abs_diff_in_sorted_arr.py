class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        partialSums = (0,) + tuple(accumulate(nums))

        answers = [
            [
                Nz * Z,
                -(partialSums[Z] - partialSums[0]),
                partialSums[len(nums)] - partialSums[Z + 1],
                -(Nz * (len(nums) - 1 - Z)),
            ]
            for Z, Nz in enumerate(nums)
        ]
        # print(f'{answers=}')
        return tuple(map(sum, answers))

# NOTE: Accepted on second Run (plus/minus parity reversal)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 700 ms Beats 5.01%
# NOTE: Memory 49.49 MB Beats 5.56%
