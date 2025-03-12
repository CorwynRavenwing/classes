class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        DEBUG = False

        LEN_S = len(s)
        indexes_by_letter = {
            'a': [],
            'b': [],
            'c': [],
        }
        for index, letter in enumerate(s):
            indexes_by_letter[letter].append(index)
        
        # print(f'{indexes_by_letter=}')

        index_of_next_occurrence = {
            'a': [None] * LEN_S,
            'b': [None] * LEN_S,
            'c': [None] * LEN_S,
        }
        for letter, indexes in indexes_by_letter.items():
            indexes = list(indexes)
            for i, value in enumerate(index_of_next_occurrence[letter]):
                if not indexes:
                    break
                index_of_next_occurrence[letter][i] = indexes[0]
                if i == indexes[0]:
                    del indexes[0]
        
        # print(f'{index_of_next_occurrence=}')

        substrings_beginning_at_index = [None] * LEN_S

        ABC_lists = index_of_next_occurrence.values()
        # print(f'{ABC_lists=}')
        for index, ABC in enumerate(zip(*ABC_lists)):
            if DEBUG: print(f'  {ABC=}')
            if None in ABC:
                substrings_beginning_at_index[index] = 0
                continue
            first = min(ABC)
            last = max(ABC)
            assert first == index
            assert substrings_beginning_at_index[index] is None
            count = LEN_S - last
            if DEBUG: print(f'    {first=} {last=} {count=}')
            substrings_beginning_at_index[index] = count
        
        if DEBUG: print(f'{substrings_beginning_at_index=}')

        return sum(substrings_beginning_at_index)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 602 ms Beats 5.38%
# NOTE: Memory 22.42 MB Beats 17.66%

# NOTE: re-ran for challenge:
# NOTE: Runtime 599 ms Beats 5.35%
# NOTE: Memory 23.34 MB Beats 17.65%
