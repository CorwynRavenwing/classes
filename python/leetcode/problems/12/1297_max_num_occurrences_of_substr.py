class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        # SHORTCUT:
        # for any substring XYZW,
        # 1) with minSize < length <= maxSize,
        # 2) with U unique characters, and 
        # 3) with N occurrences in the string;
        # THEN, any shorter substring XYZ (created by truncating the
        # last character off of XYZW) will absolutely have:
        # 1) minsize <= length <= maxSize;
        # 2) U or U-1 unique characters, and
        # 3) N or possibly more occurences in the string.
        # THEREFORE, without loss of generality we can search for
        # strings of *exactly* minSize characters.

        substrings = Counter()
        for i in range(len(s) - minSize + 1):
            if i == 0:
                fragment = s[i:i + minSize]
                letter_counts = Counter(fragment)
                print(f'[{i}]: "{fragment}"')
            else:
                A = s[i - 1]
                B = s[i - 1 + minSize]
                print(f'[{i}]: {A=} {B=}')
                if A != B:
                    letter_counts[A] -= 1
                    if not letter_counts[A]:
                        del letter_counts[A]
                    letter_counts[B] += 1
                fragment = fragment[1:] + B
                print(f'[{i}]: "{fragment}"')

            if len(letter_counts) <= maxLetters:
                print(f'  Match ({len(letter_counts)})')
                substrings[fragment] += 1
            
        print(f'{substrings=}')
        if len(substrings) == 0:
            return 0
        
        answers = substrings.most_common(1)
        print(f'{answers=}')
        assert len(answers) == 1

        (best_substring, count) = answers.pop()
        print(f'\nFound {best_substring=}')

        return count

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 442 ms Beats 25.93%
# NOTE: Memory 20.14 MB Beats 29.20%
