class Solution:

    # we borrow some code from 453:

    def minMoves(self, nums: List[int], target: int) -> int:

        # SHORTCUT: "increment or decrement 1 element"
        # === "amount by which all the other numbers differ from Target"
        # with abs() to deal with higher/lower
        return sum([
            abs(N - target)
            for N in nums
        ])

    def minMoves2(self, nums: List[int]) -> int:

        nums.sort()
        # Not actually necessary to try every option
        # possibles = [
        #     self.minMoves(nums, X)
        #     for X in range(min(nums), max(nums)+1)
        # ]
        # print(f'{possibles=}')

        # Because the median should work instead
        # ... we may need to check both semi-medians in an even array (?)
        median = nums[
            len(nums) // 2
        ]
        return self.minMoves(nums, median)

# NOTE: Accepted on first Submit
# NOTE: Runtime 64 ms Beats 97.83%
# NOTE: Memory 17.88 MB Beats 90.77%
