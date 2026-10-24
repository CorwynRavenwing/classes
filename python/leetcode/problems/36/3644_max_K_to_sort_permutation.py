class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        
        pairs = [
            (N, idx)
            for (idx, N) in enumerate(nums)
        ]
        # print(f'raw    {pairs=}')
        pairs.sort()
        # print(f'sorted {pairs=}')
        outOfPlace = [
            N
            for (i, (N, j)) in enumerate(pairs)
            if i != j
        ]
        # print(f'{outOfPlace=}')

        if not outOfPlace:
            return 0

        answers = tuple(accumulate(outOfPlace, operator.and_))
        # print(f'{answers=}')

        return answers[-1]

# NOTE: Acceptance Rate 41.0% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (edge case already sorted; Output Exceeded)
# NOTE: Runtime 148 ms Beats 5.49%
# NOTE: Memory 38.56 MB Beats 7.69%
