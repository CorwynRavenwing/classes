class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        minimum = min(nums)
        maximum = max(nums)
        min_index = nums.index(minimum)
        max_index = nums.index(maximum)

        answers = []

        min_left = min_index + 1
        max_left = max_index + 1

        min_right = len(nums) - min_index
        max_right = len(nums) - max_index

        print(f'{min_index=} {min_left=} {min_right=}')
        print(f'{max_index=} {max_left=} {max_right=}')

        # case 1: delete both from left
        answers.append(
            max(min_left, max_left)
        )

        # case 2: delete both from right
        answers.append(
            max(min_right, max_right)
        )

        # case 3: delete min from from left and max from right
        answers.append(
            min_left + max_right
        )

        # case 4: delete min from from right and max from left
        answers.append(
            min_right + max_left
        )

        print(f'{answers=}')

        return min(answers)

# NOTE: Accepted on second Run (logic error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 17 ms Beats 87.12%
# NOTE: Memory 29.75 MB Beats 7.46%
