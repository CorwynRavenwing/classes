class Solution:
    def removeStars(self, s: str) -> str:

        stack = []
        for ch in s:
            if ch == '*':
                ch = stack.pop(-1)
                # print(f'"*": pop "{ch}"')
            else:
                stack.append(ch)
                # print(f'push "{ch}"')
        return ''.join(stack)
# NOTE: Runtime 133 ms Beats 68.85%
# NOTE: Memory 18.21 MB Beats 42.67%
