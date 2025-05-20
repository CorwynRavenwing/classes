class Solution:
    def triangleType(self, nums: List[int]) -> str:

        nums.sort()
        print(f'{nums=}')

        (A, B, C) = nums

        if (A + B) <= C:
            return "none"
        
        if A == B == C:
            return "equilateral"
        
        if (A == B) or (A == C) or (B == C):
            return "isosceles"

        return "scalene"

# NOTE: re-ran for challenge:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.77 MB Beats 51.84%
# NOTE: I didn't record Runtime earlier, so this must be much faster
