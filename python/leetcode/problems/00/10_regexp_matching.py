class Solution:
    @cache
    def isMatch(self, s: str, p: str) -> bool:
        print(f'isMatch("{s}","{p}")')
        if s == p:
            print(f'  trivial True')
            return True

        if not p:
            print(f'  trivial False (P)')
            return False

        if (len(p) >= 2) and (p[1] == '*'):
            print(f'  Try Skip:')
            skipThisPattern = self.isMatch(s, p[2:])
            if skipThisPattern:
                # short-circuit following section
                return True
            print(f'  Try Use:')
            useThisPattern = (
                # nothing to match against
                False
                if not s
                else
                # drop one matching character and check the rest
                self.isMatch(s[1:], p)
                if (p[0] == s[0]) or (p[0] == '.')
                else
                # first character does not match
                False
            )
            print(f'  asterisk: {skipThisPattern} or {useThisPattern}')
            return skipThisPattern or useThisPattern
        
        if not s:
            print(f'  trivial False (S)')
            return False

        if (p[0] == s[0]) or (p[0] == '.'):
            print(f'  simple match')
            return self.isMatch(s[1:], p[1:])
        
        return False

# NOTE: Acceptance Rate: 28.4% (HARD)
# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 48 ms Beats 42.83%
# NOTE: Memory 18.81 MB Beats 11.32%
