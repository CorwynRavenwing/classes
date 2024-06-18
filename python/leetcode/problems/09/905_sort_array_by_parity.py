class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = [
            N
            for N in nums
            if N % 2 == 0
        ]
        odds = [
            N
            for N in nums
            if N % 2 != 0
        ]
        return evens + odds

