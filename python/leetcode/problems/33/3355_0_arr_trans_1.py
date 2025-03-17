class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        first = nums[0]
        last = nums[-1]
        diffs = [first] + [
            B - A
            for (A, B) in pairwise(nums)
        ] + [-last]
        # print(f'[start] {diffs=}')
        for (Li, Ri) in queries:
            diffs[Li] -= 1
            diffs[Ri + 1] += 1
            # print(f'[{Li},{Ri}] {diffs=}')
        partialSum = tuple(accumulate(diffs))
        # print(f'{partialSum=}')

        # SHORTCUT: we are told to ensure we only decrement positive numbers,
        # then look for all zeros; instead, we decrement all numbers,
        # then check that nothing is positive
        return (max(partialSum) <= 0)

# NOTE: Acceptance Rate 42.5% (medium)

# NOTE: Accepted on second Run (pos/neg parity error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 119 ms Beats 21.00%
# NOTE: Memory 55.84 MB Beats 25.26%
