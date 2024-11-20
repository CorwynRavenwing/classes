class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        def isPalindrome(x: str) -> bool:
            forward = tuple(x)
            backward = tuple(reversed(x))
            return (forward == backward)

        if len(palindrome) == 1:
            # all 1-character strings are palindromes
            return ''
        
        answer = ''
        for i, C in enumerate(palindrome):
            if C == 'a':
                continue

            # replace first non-A character with an A
            answer = palindrome[:i] + 'a' + palindrome[i + 1:]
            if isPalindrome(answer):
                answer = ''
                continue
            else:
                break
        
        if not answer:
            # all characters were A.  Replace last with a B
            answer = palindrome[:-1] + 'b'
        
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was an edge case)
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.85 MB Beats 23.34%
