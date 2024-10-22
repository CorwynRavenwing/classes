class Solution:

    # we borrow some code from #930:

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

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        binaryArray = [
            N % 2
            for N in nums
        ]

        return self.numSubarraysWithSum(binaryArray, k)

# NOTE: Re-used entire prior version with wrapper code around it
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 199 ms Beats 97.33%
# NOTE: Memory 27.90 MB Beats 6.86%
