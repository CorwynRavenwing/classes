class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(f"{s=}")
        S = list([
            ch.lower()
            for ch in list(s)
            if ch.isalnum()
        ])
        print(f"S={''.join(S)}")
        while len(S) >= 2:
            F = S.pop(0)
            L = S.pop(-1)
            if F != L:
                return False
        if len(S) == 1:
            return True
        if len(S) == 0:
            return True
        # should probably collapse both prior conditionals to 'return True'

