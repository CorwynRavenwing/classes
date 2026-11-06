class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        Max = max(nums)
        print(f'{Max=}')
        increases = [
            Max - N
            for N in nums
        ]
        print(f'{increases=}')
        return sum(increases)

# NOTE: Acceptance Rate 82.0% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 1 ms Beats 57.44%
# NOTE: Memory 19.40 MB Beats 11.54%
