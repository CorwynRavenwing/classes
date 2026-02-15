class Solution:
    def addBinary(self, a: str, b: str) -> str:

        print(f"{a=} {b=}")
        A = list(map(int, list(a)))
        B = list(map(int, list(b)))
        print(f"{A=} {B=}")
        changed = False
        while len(A) < len(B):
            A = [0] + A
            changed = True
        while len(B) < len(A):
            B = [0] + B
            changed = True
        if changed:
            print(f"{A=} {B=}")
        Z = list(zip(A, B))
        print(f"{Z=}")
        C = list(map(sum, Z))
        while max(C) >= 2:
            print(f"{C=}")
            if C[0] >= 2:
                C = [0] + C
                continue
            index = C.index(max(C))
            carry = C[index] // 2
            C[index - 1] += carry
            C[index] -= carry * 2
        print(f"{C=}")
        return ''.join(map(str, C))

# NOTE: Acceptance Rate 56.9% (easy)

# NOTE: re-ran for challenge:
# NOTE: Runtime 75 ms Beats 5.47%
# NOTE: Memory 19.83 MB Beats 12.44%
