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

# NOTE: re-ran for challenge:
# NOTE: Runtime 89 ms Beats 8.63%
# NOTE: Memory 18.19 MB Beats 9.35%
