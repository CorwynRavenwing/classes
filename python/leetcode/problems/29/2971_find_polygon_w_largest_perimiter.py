class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()

        partialSums = (0,) + tuple(accumulate(nums))
        print(f'{partialSums=}')

        stuffToZip = [
            nums,               # longest side
            partialSums[:-1],   # sum of shorter sides
            partialSums[1:],    # sum of all sides
        ]
        data = tuple(zip(*stuffToZip))
        data_GE_3_sides = data[2:]
        for (N, otherSides, allSides) in reversed(data_GE_3_sides):
            print(f'{N=} {otherSides=} {allSides=}')
            if N < otherSides:
                return allSides

        return -1

# NOTE: Accepted on first Submit
# NOTE: Runtime 628 ms Beats 5.06%
# NOTE: Memory 38.52 MB Beats 6.11%
