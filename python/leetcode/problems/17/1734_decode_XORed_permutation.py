class Solution:
    def decode(self, encoded: List[int]) -> List[int]:

        L = len(encoded) + 1
        perm = [None] * L

        X = 0
        for i in range(1, L + 1):
            X ^= i  # "^" == XOR
        # X now contains XOR(1, 2, 3, 4, 5, ...), === XOR(original_array)
        OddEncoded = 0
        for i in range(1, L, 2):
            # odd-numbered locations only
            OddEncoded ^= encoded[i]

        # say length is 5 and perm is (A,B,C,D,E).
        # so encoded is (AB,BC,CD,DE).
        # X = XOR(1,2,3,4,5) === XOR(perm) === XOR(A,B,C,D,E)
        # OddEncoded === (BCDE), that is, everything but A.
        # X ^ OddEncoded == ABCDE ^ BCDE which === A back again!
        perm[0] = X ^ OddEncoded
        for i in range(L - 1):
            perm[i + 1] = perm[i] ^ encoded[i]

        return perm

