class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        for digit in map(str, reversed(range(10))):
            print(f'{digit=}')
            three = digit * 3
            print(f'  {three=}')
            if three in num:
                return three
        return ""

# NOTE: Acceptance Rate 69.4% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.94 MB Beats 17.55%
