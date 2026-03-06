class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        if '1' not in s:
            # entire number must be '0'
            return True

        if '0' not in s:
            # entire number is made of '1's
            return True
        
        zero_index = s.index('0')
        if '1' not in s[zero_index:]:
            # after first zero, everything else is '0's
            return True
        
        return False

# NOTE: Acceptance Rate 40.3% (easy)

# NOTE: re-ran for challenge:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.21 MB Beats 77.09%
