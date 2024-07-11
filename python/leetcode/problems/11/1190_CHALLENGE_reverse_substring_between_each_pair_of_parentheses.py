class Solution:
    def reverseParentheses(self, s: str) -> str:

        def revStr(s: str) -> str:
            return ''.join(
                reversed(s)
            )

        L = -1
        R = -1
        print(f'{s=}')
        # if ')' not in s:
        #     print(f'  DONE')
        #     return s
        for i, C in enumerate(s):
            # print(f'  [{i}]{C}')
            if C == '(':
                # print(f'    LP')
                L = i
            elif C == ')':
                # print(f'    RP')
                R = i
                print(f'    Reversing string {L} .. {R}')
                left = s[:L]
                LP = s[L]
                mid = s[L+1:R]
                RP = s[R]
                right = s[R+1:]
                print(f'  "{left}<{mid}>{right}"')
                s = left + revStr(mid) + right
                # print(f'  "{s}"')
                return self.reverseParentheses(s)
        print(f'  DONE')
        return s

