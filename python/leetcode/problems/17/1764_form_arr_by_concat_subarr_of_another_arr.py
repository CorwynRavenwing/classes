class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:

        pointer = -1
        for i, group in enumerate(groups):
            first_item_in_group = group[0]
            group_len = len(group)
            while True:
                try:
                    pointer = nums.index(first_item_in_group, pointer + 1)
                except ValueError:
                    return False
                fragment = nums[pointer:pointer + group_len]
                if group == fragment:
                    # skip past the fragment we just matched
                    pointer += group_len - 1
                    break
        return True

# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.50 MB Beats 11.69%
