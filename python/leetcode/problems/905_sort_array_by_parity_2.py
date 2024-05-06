class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
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
        both = zip(evens, odds)
        flatten = [
            val
            for T in both
            for val in T
        ]
        return flatten

