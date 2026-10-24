class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        
        # cheap way: sort, find values EQ target, return indexes.

        # right way:
        # LT = count numbers < target
        LT = sum(
            1 if N < target else 0
            for N in nums
        )
        # EQ = count numbers == target
        EQ = sum(
            1 if N == target else 0
            for N in nums
        )
        print(f'{LT=} {EQ=}')
        # first index = (LT)
        # last index = (LT+EQ)
        return tuple(
            range(LT, LT + EQ)
        )

# NOTE Acceptance Rate 78.5% (easy)

# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 2 ms Beats 26.99%
# NOTE: Memory 19.24 MB Beats 62.71%
