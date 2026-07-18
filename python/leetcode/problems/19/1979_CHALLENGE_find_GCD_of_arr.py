class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        # Euclidian Algorithm for GCD, as described in Wikipedia
        def GCD(A: int, B: int) -> int:
            # print(f'GCD({A},{B})')
            if B == 0:
                return A
            else:
                return GCD(B, A % B)
        
        return GCD(
            min(nums),
            max(nums)
        )

# NOTE: Acceptance Rate 80.3% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.42 MB Beats 11.34%
