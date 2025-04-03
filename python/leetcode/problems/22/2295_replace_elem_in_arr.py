class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_of = {
            value: index
            for index, value in enumerate(nums)
        }
        # print(f'{index_of=}')

        for old, new in operations:
            index = index_of[old]
            nums[index] = new
            index_of[new] = index
            index_of[old] = None
            # print(f'[{old}:{new}] {nums}')

        return nums

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 69 ms Beats 46.31%
# NOTE: Memory 70.18 MB Beats 68.96%
