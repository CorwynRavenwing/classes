class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # "12" in base (N-2)
        # == 1 * (N-2) + 2 * (1)
        # == N - 2 + 2
        # == N.
        # Therefore N in base N-2 is always "12", for all base > 2 (N > 4)
        # and obviously, "12" is not a palindrome.
        # for N == 4: 4 in base 2 is "100", which is not a palindrome.
        # Therefore *THERE ARE NO* "strictly palindromic" numbers.
        return False

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.84 MB Beats 30.73%
