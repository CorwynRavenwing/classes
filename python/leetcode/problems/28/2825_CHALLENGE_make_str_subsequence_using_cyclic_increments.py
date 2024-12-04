class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        Rotate = lambda x: alphabet[
            (alphabet.index(x) + 1) % len(alphabet)
        ]

        i = 0
        j = 0
        while (i < len(str1)) and (j < len(str2)):
            A = str1[i]
            B = str2[j]
            Z = Rotate(A)
            print(f'[{i}][{j}] {A} {Z} {B}')
            if A == B or Z == B:
                i += 1
                j += 1
            else:
                i += 1
        if j < len(str2):
            print(f'Failed at {j=} "{str2[j:]}"')
            return False
        print(f'Succeed')
        return True

# NOTE: Runtime 472 ms Beats 5.20%
# NOTE: Memory 17.76 MB Beats 12.40%
# NOTE: re-ran for challenge, and recieved:
# NOTE: Runtime 452 ms Beats 5.56%
# NOTE: Memory 17.90 MB Beats 5.69%
# NOTE: about the same, though memory percent is much worse
