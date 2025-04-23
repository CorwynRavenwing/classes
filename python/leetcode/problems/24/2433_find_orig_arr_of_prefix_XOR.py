class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        # [A, A^B, A^B^C, A^B^C^D]
        # XOR adjacent elements:
        # [A ^ A^B, A^B ^ A^B^C, A^B^C ^ A^B^C^D]
        # combine similar letters:
        # [A^A ^ B, A^A ^ B^B ^ C, A^A ^ B^B ^ C^C ^ D]
        # pairs cancel because XOR is its own inverse
        # [B, C, D]
        # then add [A] to the front.

        answer = tuple([
            X ^ Y
            for X, Y in pairwise(pref)
        ])
        A = pref[0]
        return (A,) + answer

# NOTE: Accepted on third Run (math error, typo, argument count error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 22 ms Beats 80.75%
# NOTE: Memory 35.66 MB Beats 27.02%
