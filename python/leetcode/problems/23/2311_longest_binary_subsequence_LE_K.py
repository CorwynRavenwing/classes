class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:

        def valueOfBinary(s: str) -> int:
            return int(s, 2)

        print(f'{s} {valueOfBinary(s)} {k}')
        while valueOfBinary(s) > k:
            s = s.replace('1', '', 1)   # delete first '1'
            print(f'{s} {valueOfBinary(s)} {k}')
        
        return len(s)
# NOTE: Runtime 126 ms Beats 10.65%
# NOTE: Memory 16.70 MB Beats 27.81%
