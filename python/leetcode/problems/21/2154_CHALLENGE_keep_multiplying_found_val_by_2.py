class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        nums = set(nums)
        N = original
        print(f'{N}')
        while N in nums:
            N *= 2
            print(f'{N}')
        
        return N

# NOTE: Acceptance Rate 72.0% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 1 ms Beats 26.25%
# NOTE: Memory 18.08 MB Beats 12.78%
