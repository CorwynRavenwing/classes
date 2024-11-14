class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # we borrow some code from #1047:

        stack = []
        for C in s:
            stack.append(C)
            if stack and (stack[-k:] == [C] * k):
                # print(''.join(stack))
                stack = stack[:-k]
            # print(''.join(stack))
        return ''.join(stack)

# NOTE: Accepted on second Run (first was fencepost error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 5772 ms Beats 5.10%
# NOTE: Memory 18.42 MB Beats 91.36%
