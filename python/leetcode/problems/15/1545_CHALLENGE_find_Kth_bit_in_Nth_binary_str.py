class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        print(f'KB?({n},{k}')

        if n == 1:
            assert k == 1
            return '0'

        NOT = lambda x: (
            '0' if x == '1' else
            '1' if x == '0' else
            '?'
        )

        # PROCESS:
        # L === length of Si+1 == (2 ** i)      e.g. len(S4)+1 = 2^4 = 16 
        # H === half the length == 2 ** (i - 1) e.g. halflen(S4) = 2^3 = 8
        # section 1  section2  section 3
        # Si[0:H]    Si[H]     Si[H+1:L]

        L = 2 ** n
        H = 2 ** (n - 1)    # === L // 2

        if 0 <= k < H:
            return self.findKthBit(n - 1, k)
        elif k == H:
            return '1'
        elif H < k < L:
            print(f'invert:')
            return NOT(
                self.findKthBit(n - 1, L - k)
            )
        else:
            raise Exception(f'assert {0=} < {k=} < {L=}')

# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.70 MB Beats 56.21%
