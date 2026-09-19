class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        def endpoints_are_palindrome(i: int, j: int) -> bool:
            if i >= j:
                # don't randomly call this function with value
                # where i > j or it will give false positives
                return True
            try:
                A = s[i]
                B = s[j]
            except IndexError:
                return False
            if A != B:
                return False
            return endpoints_are_palindrome(i + 1, j - 1)
        
        # greedy algorithm will hopefully work:
        answer = 0
        L = R = 0
        while L < len(s):
            Rmin = L + k - 1
            for R in [Rmin, Rmin + 1]:
                print(f'[{L}:{Rmin}={R}]: ')
                print(f'  frag={s[L:R+1]}')
                if endpoints_are_palindrome(L, R):
                    print(f'  yes')
                    answer += 1
                    L = R
                    break
                else:
                    print(f'  no')
                    continue
            L += 1
        
        return answer

# NOTE: Acceptance Rate 46.0% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Run (fencepost errors)
# NOTE: Runtime 23 ms Beats 51.03%
# NOTE: Memory 19.42 MB Beats 59.79%
