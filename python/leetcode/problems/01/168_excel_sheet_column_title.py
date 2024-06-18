class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        N = [columnNumber]
        while max(N) > 26:
            print(f"{N=}")
            if N[0] > 26:
                N = [0] + N
                continue
            index = N.index(max(N))
            carry = N[index] // 26
            if N[index] % 26 == 0:
                carry -= 1
            N[index - 1] += carry
            N[index] -= carry * 26
        print(f"{N=}")
        ascii_base = ord('A') - 1
        L = list([
            chr(ascii_base + val)
            for val in N
        ])
        print(f"{L=}")
        return ''.join(L)

