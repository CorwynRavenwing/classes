class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        # per the Hints, we are making DP[i] the longest subsequence
        # whose last NUMBER is i, as opposed to the last INDEX.
        DP = {}

        for A in arr:
            # process elements left to right
            B = A - difference
            print(f'{A=} {B=}')
            if B in DP:
                DP[A] = DP[B] + 1
            else:
                DP[A] = 1
            print(f'  {DP[A]=}')
        
        return max(DP.values())

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 333 ms Beats 5.26%
# NOTE: Memory 27.98 MB Beats 74.86%
