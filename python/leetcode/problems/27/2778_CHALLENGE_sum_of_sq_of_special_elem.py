class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:

        n = len(nums)
        
        specials = [
            value
            for i, value in enumerate(nums)
            if n % (i+1) == 0
        ]
        print(f'{specials=}')

        squares = [
            x * x
            for x in specials
        ]
        print(f'{squares=}')

        return sum(squares)

# NOTE: Acceptance Rate 82.4% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.37 MB Beats 14.08%
