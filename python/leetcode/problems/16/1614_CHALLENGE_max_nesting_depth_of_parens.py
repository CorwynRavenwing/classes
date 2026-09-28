class Solution:
    def maxDepth(self, s: str) -> int:
        
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(depth, max_depth)
                print(f'open: {depth=}')
            elif char == ')':
                depth -= 1
                print(f'open: {depth=}')

        return max_depth

# NOTE: Acceptance Rate 85.2% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.18 MB Beats 85.25%
