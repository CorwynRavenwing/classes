class Solution:
    def doesAliceWin(self, s: str) -> bool:

        vowels = 'aeiou'
        
        counts = Counter(s)
        print(f'{counts=}')
        vowel_count = sum([
            count
            for letter, count in counts.items()
            if letter in vowels
        ])
        print(f'{vowel_count=}')

        # if vowel count is zero, Alice loses
        if not vowel_count:
            return False
        
        # if vowel count is odd, Alice takes everthing and wins
        if vowel_count % 2 == 1:
            return True
        
        # otherwise, vowel count is even.
        # Alice takes any move whatsoever: assume she takes one vowel.
        vowel_count -= 1
        # Bob takes any move whatsoever: assume he takes two vowels.
        vowel_count -= 2

        # if vowel count is odd, Alice takes everthing and wins
        if vowel_count % 2 == 1:
            return True

        raise Exception('Spoiler alert: the vowel count will ALWAYS be odd here.')

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 98 ms Beats 36.15%
# NOTE: Memory 17.48 MB Beats 50.88%
