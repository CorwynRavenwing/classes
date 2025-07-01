class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        counts = Counter(nums)
        digits = tuple(sorted(counts.keys()))
        # print(f'{digits=}')

        harmonious = [
            (A, B)
            for (A, B) in pairwise(digits)
            if B - A == 1
        ]
        # print(f'{harmonious=}')

        answers = [
            counts[A] + counts[B]
            for (A, B) in harmonious
        ]
        # print(f'{answers=}')

        return max(answers, default=0)

# NOTE: Acceptance Rate 57.8% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 31 ms Beats 56.05%
# NOTE: Memory 19.29 MB Beats 21.92%
