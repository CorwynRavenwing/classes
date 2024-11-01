class Solution:
    def isValid(self, s: str) -> bool:
        
        # brute force method:
        while 'abc' in s:
            s = s.replace('abc', '')
            print(f'{s=}')

        return (s == '')

        # stack method:
        stack = []
        for char in s:
            stack.append(char)
            # print(f'push {stack=}')
            if stack[-3:] == ['a', 'b', 'c']:
                stack = stack[:-3]
                # print(f'pop: {stack=}')

        return stack == []

# NOTE: brute force method:
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 4 ms Beats 83.33%
# NOTE: Memory 16.50 MB Beats 99.79%

# NOTE: stack method:
# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 87 ms Beats 6.41%
# NOTE: Memory 16.94 MB Beats 14.96%

# NOTE: Brute force method is MUCH better!
