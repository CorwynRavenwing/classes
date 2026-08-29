class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        
        nums = set(nums)
        N = k
        while N in nums:
            print(f'{N=}')
            N += k
        print(f'{N=} (no)')
        return N

# NOTE: Acceptance Rate 64.2% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 20.84%
# NOTE: Memory 19.44 MB Beats 2.48%
