class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        digits = tuple(map(len, map(str, nums)))
        print(f'{digits=}')

        even = [
            D
            for D in digits
            if D % 2 == 0
        ]
        print(f'{even=}')

        return len(even)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 38.79%
# NOTE: Memory 18.04 MB Beats 9.44%
