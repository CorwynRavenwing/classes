class Solution:
    def clearDigits(self, s: str) -> str:
        
        digits = '0123456789'
        stack = []
        for char in s:
            if char in digits:
                if stack:
                    popped = stack.pop()
                else:
                    popped = '(empty)'
                print(f'{char=} digit: {popped=}')
            else:
                stack.append(char)
                print(f'{char=} non-digit: push')
        return ''.join(stack)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 30.49%
# NOTE: Memory 17.84 MB Beats 27.31%
