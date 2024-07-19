class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:

        vowels = 'aeiou'
        dups = [
            ch + ch
            for ch in vowels
        ]
        next = [
            A + B
            for (A, B) in zip(vowels, vowels[1:])
        ]
        allowed = dups + next

        # print(f'replace "ua"')
        # word = word.replace('ua', 'u|a')    # end of one, beginning of another
        # for ch in vowels:
        #     check = ch + 'a'
        #     if check not in allowed:
        #         print(f'replace "{check}"')
        #         word = word.replace(check, '|a')
        #     check = 'u' + ch
        #     if check not in allowed:
        #         print(f'replace "{check}"')
        #         word = word.replace(check, 'u|')
        for A in vowels:
            for B in vowels:
                check = A + B
                if check not in allowed:
                    replacement = (
                        (
                            A if A == vowels[-1] else ''
                        ) + '|' + (
                            B if B == vowels[0] else ''
                        )
                    )
                    print(f'{check}->"{replacement}"')
                    word = word.replace(check, replacement)
                    while check in word:
                        print(f'  again')
                        word = word.replace(check, replacement)
                else:
                    print(f'{check} OK')

        print(f'{word=}')

        possibles = [
            test
            for test in word.split('|')
            if test
            if test[0] == vowels[0]
            if test[-1] == vowels[-1]
        ]
        print(f'{possibles=}')

        lengths = map(len, possibles)
        return max(lengths, default=0)
# NOTE: Runtime 137 ms; Beats 98.81%
# NOTE: Memory 22.88 MB; Beats 21.43%
