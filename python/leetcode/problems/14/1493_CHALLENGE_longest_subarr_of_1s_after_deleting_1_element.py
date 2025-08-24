class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        numbers_and_counts = [
            (key, len(tuple(values)))
            for key, values in groupby(nums)
        ]
        print(f'{numbers_and_counts=}')

        single_zero = (0, 1)
        while single_zero in numbers_and_counts:
            numbers_and_counts.remove(single_zero)
        print(f'{numbers_and_counts=}')

        counts = [
            (
                count
                if (number == 1)
                else 0
            )
            for (number, count) in numbers_and_counts
        ]
        print(f'{counts=}')

        if len(counts) == 1:
            pairs = counts
        else:
            pairs = [
                A + B
                for A, B in pairwise(counts)
            ]
        print(f'{pairs=}')

        answer = max(pairs, default=0)

        if 0 not in nums:
            return answer - 1
        else:
            return answer

# NOTE: Acceptance Rate 69.5% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was edge case with no 1's)
# NOTE: Runtime 15 ms Beats 98.78%
# NOTE: Memory 21.44 MB Beats 5.66%

# NOTE: re-ran for challenge:
# NOTE: Runtime 15 ms Beats 98.36%
# NOTE: Memory 22.77 MB Beats 6.20%
