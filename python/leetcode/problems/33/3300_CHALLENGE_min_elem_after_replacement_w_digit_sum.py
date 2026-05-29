class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        DIGITSUM = lambda x: sum(map(int, str(x)))

        sums = tuple(map(DIGITSUM, nums))
        print(f'{sums=}')

        return min(sums)

# NOTE: Acceptance Rate 84.8% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 11 ms Beats 6.88%
# NOTE: Memory 19.23 MB Beats 56.38%
