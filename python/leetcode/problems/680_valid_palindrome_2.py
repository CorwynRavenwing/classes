class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(L: List[str]) -> bool:
            return L == list(reversed(L))
        
        L = list(s)
        if is_palindrome(L):
            print("already")
            return True
        while L:
            # print(f"{L=}")
            if L[0] == L[-1]:
                # print(f"  '{L[0]}' skip")
                L = L[1:-1]
            else:
                print(f"  '{L[0]}' != '{L[-1]}'")
                if is_palindrome(L[1:]):
                    print("    YES, delete char 0")
                    return True
                if is_palindrome(L[:-1]):
                    print("    YES, delete char -1")
                    return True
                print("    NO, neither works")
                return False
        # print(f"{L=}")
        return True

