class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        for C in s:
            if stack and (stack[-1] == C):
                stack.pop(-1)
                continue
            else:
                stack.append(C)
        return ''.join(stack)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 20 ms Beats 54.50%
# NOTE: Memory 17.71 MB Beats 28.50%
