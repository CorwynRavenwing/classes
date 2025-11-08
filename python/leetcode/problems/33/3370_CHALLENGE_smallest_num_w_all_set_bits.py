class Solution:
    def smallestNumber(self, n: int) -> int:
        
        # NOTE 1: The smallest number GE n such that
        # it contains all set bits, === the number of the
        # same (binary) length consisting of all ones.

        # NOTE 2: the number of length Z consisting of all ones
        # === (2 ^ Z) - 1

        bin_n = f'{n:b}'
        print(f'{bin_n=}')
        len_n = len(bin_n)
        print(f'{len_n=}')
        answer = (2 ** len_n) - 1

        return answer

# NOTE: Acceptance Rate 76.5% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 4 ms Beats 11.72%
# NOTE: Memory 17.83 MB Beats 26.92%
