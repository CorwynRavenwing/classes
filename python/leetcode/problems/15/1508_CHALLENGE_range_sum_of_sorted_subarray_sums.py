class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        mod = 10 ** 9 + 7

        partialSums = tuple(accumulate(nums))
        # print(f'{partialSums=}')

        computed_array = list(partialSums) + [
            Right - Left
            for indexL, Left in enumerate(partialSums)
            for Right in partialSums[indexL + 1:]
        ]
        computed_array.sort()
        # print(f'{computed_array=}')

        computedPartialSums = tuple(accumulate(computed_array))
        # print(f'{computedPartialSums=}')

        left -= 1   # zero-basis
        right -= 1

        answer = (
            (
                computedPartialSums[right]
            ) - (
                computedPartialSums[left - 1]
                if left > 0
                else 0
            )
        )

        return answer % mod
# NOTE: Runtime 211 ms Beats 80.53%
# NOTE: O(N^2 log(N))
# NOTE: Memory 64.96 MB Beats 5.75%
# NOTE: O(N^2)
