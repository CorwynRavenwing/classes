class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        print(f'{len(s)=}')
        
        stack = []
        right_end_of = {}
        for i, ch in enumerate(s):
            if ch == '(':
                # print(f'push {i=}')
                stack.append(i)
                continue
            if ch == ')':
                assert stack, f'unbalanced right-paren at {i}'
                j = stack.pop(-1)
                # print(f'pop {j=} {i=}')
                right_end_of[j] = i
        assert not stack, f'unbalanced left-parens at {stack}'
        print(f'{right_end_of=}')

        pairs = []

        i = 0
        while i < len(s):
            j = right_end_of[i]
            pairs.append( (i, j) )
            i = j + 1
        print(f'{pairs=}')

        frags = [
            s[i+1:j]
            for (i, j) in pairs
        ]
        print(f'{frags=}')

        reconstruct = '(' + ')('.join(frags) + ')'
        assert s == reconstruct, f'{s=} != {reconstruct}'

        return ''.join(frags)

# NOTE: Acceptance Rate 87.5% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 13 ms Beats 5.54%
# NOTE: Memory 20.27 MB Beats 8.63%
