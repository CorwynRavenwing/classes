class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        counts = Counter(nums)
        lonely = [
            N
            for N, count in counts.items()
            if count == 1
            if counts[N - 1] == 0
            if counts[N + 1] == 0
        ]
        return lonely

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 179 ms Beats 23.34%
# NOTE: Memory 40.00 MB Beats 44.96%
