class Solution:
    def smallestString(self, s: str) -> str:

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        prevChar = lambda x: (
            alphabet[
                (alphabet.index(x) - 1) % 26
            ]
        )
        # print(f'{prevChar("q")=}')    # -> 'p'
        # print(f'{prevChar("a")=}')    # -> 'z'

        def translate(s: str) -> str:
            return ''.join([
                prevChar(C)
                for C in s
            ])

        if 'a' not in s:
            print(f'No "a": just translate')
            return translate(s)

        frontAgroup = ''
        while s.startswith('a'):
            # move 1 'a' from s to frontAgroup
            frontAgroup += 'a'
            s = s[1:]
        if frontAgroup:
            print(f'moved {len(frontAgroup)} "a" from front')
        
        if not s:
            print(f'input was entirely made of "a": move 1 back to become a "z"')
            # move 1 'a' back into s
            s = 'a'
            frontAgroup = frontAgroup[:-1]
            return frontAgroup + translate(s)

        if 'a' not in s:
            print(f'all "a" were in front group: translate remainder')
            return frontAgroup + translate(s)

        index = s.index('a')
        print(f'Translate section [0:{index}]')
        return frontAgroup + translate(s[:index]) + s[index:]
# NOTE: Runtime 2493 ms Beats 5.15%
# NOTE: Memory 23.32 MB Beats 20.10%
