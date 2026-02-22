class Solution:
    def binaryGap(self, n: int) -> int:
        
        # NOTE: "longest distance between 1's (as defined)"
        #       === "longest run of zeros, plus 1"
        #       ... not counting trailing zeros

        binary = f'{n:b}'
        print(f'{binary=}')

        binary_no_trailing_zero = binary.rstrip('0')
        print(f'{binary_no_trailing_zero=}')

        splits = binary_no_trailing_zero.split('1')
        print(f'{splits=}')
        if len(splits) <= 2:
            return 0

        lengths = tuple(map(len, splits))
        print(f'{lengths=}')

        return max(lengths) + 1

# NOTE: Acceptance Rate 66.2% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case with trailing zeros)
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.21 MB Beats 69.40%
