class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        # s = tuple(word)
        s = word

        letters_and_counts = [
            (key, len(tuple(values)))
            for key, values in groupby(s)
        ]
        print(f'{letters_and_counts=}')

        possible_additions = [
            count - 1
            for letter, count in letters_and_counts
        ]
        print(f'{possible_additions=}')

        return sum(possible_additions) + 1

# NOTE: Acceptance Rate 58.1% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 31 ms Beats 92.39%
# NOTE: Memory 18.23 MB Beats 6.48%
