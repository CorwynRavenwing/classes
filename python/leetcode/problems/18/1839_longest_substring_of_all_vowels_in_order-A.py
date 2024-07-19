class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:

        LEGAL_PAIRS = ['Xa', 'aa', 'ae', 'ee', 'ei', 'ii', 'io', 'oo', 'ou', 'uu']
        LAST = 'u'
        best = 0
        prior = 'X'
        length = 0
        for char in word:
            print(f'{char}')
            if f'{prior}{char}' in LEGAL_PAIRS:
                length += 1
                print(f'  {length=}')
                if char == LAST:
                    best = max(best, length)
                    print(f'    ...')
                prior = char
            else:
                print(f'  nope')
                length = 0
                prior = 'X'

        return best
# NOTE: seems straightforward, but testcase 86 gives wrong answer
# and is too large to work out why manually (2169-char answer)
