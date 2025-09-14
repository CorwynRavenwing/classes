class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        vowels = 'aeiou'
        is_vowel = lambda C: (C in vowels)

        s_vowels = ''.join([C for C in s if is_vowel(C)])
        s_consonants = ''.join([C for C in s if not is_vowel(C)])

        c_consonants = Counter(s_consonants)

        def max_freq_letter(s: str) -> Tuple[str,int]:
            counts = Counter(s)
            try:
                (max_freq,) = counts.most_common(1)
            except ValueError:
                max_freq = ('', 0)
            return max_freq

        def max_freq_letter_freq(s: str) -> int:
            (letter, count) = max_freq_letter(s)
            print(f'{letter=} {count=}')
            return count

        f_vowels = max_freq_letter_freq(s_vowels)
        f_consonants = max_freq_letter_freq(s_consonants)

        print(f'{f_vowels=} {f_consonants=}')

        return f_vowels + f_consonants

# NOTE: Acceptance Rate 88.1% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 15 ms Beats 15.17%
# NOTE: Memory 17.93 MB Beats 20.04%
