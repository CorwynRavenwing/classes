class Solution:
    def splitString(self, s: str) -> bool:

        print(f'{s=}')
        while s and s[0] == '0':
            s = s[1:]   # throw away leading zeros
            print(f'{s=}')
        
        if not s:
            print(f'S was all zeros')
            return False
        
        for i in range(1, len(s)):
            t = s[:i]
            u = s[i:]
            print(f'  {i}: "{t}" "{u}"')
            ready = False
            num = int(t)
            while u:
                while u and u[0] == '0' and u != '0':
                    u = u[1:]   # throw away leading zeros except number "0"
                    print(f'    {u=}')
                num -= 1
                numStr = str(num)
                if u.startswith(numStr):
                    print(f'  ->{num=}')
                    ready = True
                    u = u[len(numStr):]
                else:
                    ready = False
                    break   # break u; next i
            # wend u
            if ready and not u:
                print(f'Success!')
                return True
        # next i

        return False
# NOTE: Runtime 34 ms; Beats 83.00%
