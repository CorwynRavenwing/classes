class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        def reversed_str(s: str) -> str:
            return ''.join(
                reversed(s)
            )

        def is_palindrome(s: str) -> bool:
            return reversed_str(s) == s
        
        L = list(s)
        add_front = []
        RL = list(reversed(L))
        print(f"#len(AF)={len(add_front)} {len(L)=}")
        while not L == RL:
            if not L:
                print(f"# ERRORING: {L=} {RL=}")
            last_letter_of_L = L.pop()
            print(f"# LLL='{last_letter_of_L}'")
            add_front.append(last_letter_of_L)
            RL = list(reversed(L))
            print(f"#len(AF)={len(add_front)} {len(L)=}")
        
        test = ''.join(
            add_front + L + list(reversed(add_front))
        )
        if not is_palindrome(test):
            print("ERROR: test is not a palindrome")
            return "ERROR"
        return test

# NOTE: Runtime 2260 ms Beats 5.64%
# NOTE: Memory 18.28 MB Beats 29.57%
