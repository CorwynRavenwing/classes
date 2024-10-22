class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        prefixSums = (0,) + tuple(accumulate(nums))
        print(f'{prefixSums=}')

        counts = Counter(prefixSums)
        print(f'{counts=}')

        answers = []
        for value, count in counts.items():
            if goal == 0:
                # Triangle:
                answers.append(count * (count - 1) // 2)
            else:
                # Multiply:
                answers.append(count * counts[goal + value])
        print(f'{answers=}')

        return sum(answers)

# NOTE: Runtime 47 ms Beats 97.51%
# NOTE: Memory 24.62 MB Beats 7.53%
