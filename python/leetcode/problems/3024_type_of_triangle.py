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

