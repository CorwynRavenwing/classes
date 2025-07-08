class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        
        # NOTES:
        #
        # for all i,j,k where i != j, examine the XOR of these values:
        # (define A, B, C === nums[i], nums[j], nums[k])
        # effective(i, j, k) ^ effective(j, i, k)
        # = (A | B) & C  ^  (B | A) & C
        # = 0 because these values will be identical.
        #
        # therefore all contributing values will be of type i==j.
        #
        # for all i,i,k where i != k, examine the XOR of these values:
        # effective(i, i, k) & effective(k, k, i)
        # = (A | A) & C  ^ (C | C) & A
        # = A & C  ^  C & A
        # = 0 because these values will be identical.
        #
        # therefore all contributing values will be of type i==j==k
        #
        # therefore, the answer is found by XORing all the answers to:
        # effective(i, i, i)
        # = (A | A) & A
        # = A & A
        # = A
        # THEREFORE, the answer is found by XORing all the values once.
        return reduce(xor, nums)
        # yes, a 1-line answer with 27 lines of comment :-)

# NOTE: Acceptance Rate 69.4% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 97.37%
# NOTE: Memory 30.27 MB Beats 1.50%
