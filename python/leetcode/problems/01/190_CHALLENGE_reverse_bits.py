class Solution:
    def reverseBits(self, n: int) ->int:
        
        binary = f'{n:032b}'
        print(f'{binary=}')
        yranib = ''.join(reversed(binary))
        print(f'{yranib=}')

        return int(yranib, 2)

# NOTE: Accepted on second Run (vague problem definition, "reverse" vs "invert")
# NOTE: Accepted on first Submit
# NOTE: Runtime 35 ms Beats 83.02%
# NOTE: Memory 18.00 MB Beats 15.22%

# NOTE: Acceptance Rate 67.2% (easy)

# NOTE: re-ran for challenge:
# NOTE: Runtime 53 ms Beats 10.78%
# NOTE: Memory 19.33 MB Beats 22.24%
