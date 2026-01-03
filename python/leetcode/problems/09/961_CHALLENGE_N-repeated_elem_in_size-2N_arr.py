class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        counts = Counter(nums)
        print(f'{counts=}')

        dups = [
            value
            for value, count in counts.items()
            if count > 1
        ]
        print(f'{dups=}')

        return dups.pop()

# NOTE: Acceptance Rate 78.3% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 26 ms Beats 6.72%
# NOTE: Memory 19.18 MB Beats 8.43%
