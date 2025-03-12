class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        vowels = 'aeiou'
        is_vowel = lambda x: (x in vowels)

        consonant_locations = [
            (0 if is_vowel(char) else 1)
            for char in word
        ]
        # print(f'{consonant_locations=}')
        vowel_locations = {
            vowel: [
                (1 if char == vowel else 0)
                for char in word
            ]
            for vowel in vowels
        }
        # print(f'{vowel_locations=}')
        ACC = lambda LIST: (0,) + tuple(accumulate(LIST))
        consonant_count = ACC(consonant_locations)
        # print(f'{consonant_count=}')
        vowel_count = {
            vowel: ACC(location_list)
            for vowel, location_list in vowel_locations.items()
        }
        # print(f'{vowel_count=}')

        def indexes_by_value(nums: List[int]) -> Dict[int,List[int]]:
            indexesByValue = {}
            for index, value in enumerate(nums):
                indexesByValue.setdefault(value, [])
                indexesByValue[value].append(index)
            # print(f'{indexesByValue=}')
            return indexesByValue
        
        consonant_indexes = indexes_by_value(consonant_count)
        consonant_first_index = {}
        consonant_last_index = {}
        for value, indexes in consonant_indexes.items():
            consonant_first_index[value] = indexes[0]
            consonant_last_index[value] = indexes[-1]
        # print(f'{consonant_first_index=}')
        # print(f'{consonant_last_index=}')
        vowel_first_index = {
            vowel: {}
            for vowel in vowels
        }
        for vowel in vowels:
            counts_for_vowel = vowel_count[vowel]
            vowel_indexes = indexes_by_value(counts_for_vowel)
            for value, indexes in vowel_indexes.items():
                vowel_first_index[vowel][value] = indexes[0]
        # print(f'{vowel_first_index=}')

        answer = 0
        for i in range(len(word)):
            # print(f'[{i}]:')
            consonants_i = consonant_count[i]
            consonants_K = consonants_i + k
            # consonants_left_old = bisect_left(consonant_count, consonants_K)
            # consonants_right_old = bisect_right(consonant_count, consonants_K)
            try:
                consonants_left = consonant_first_index[consonants_K]
                consonants_right = consonant_last_index[consonants_K] + 1
                # print(f'  (got consonants correctly)')
            except KeyError:
                consonants_left = len(word) + 1
                consonants_right = len(word) + 1
                # print(f'  (got consonants in error handler)')
            # if consonants_left_old != consonants_left or consonants_right_old != consonants_right:
            #     raise Exception(f'ERROR: {consonants_left_old} != {consonants_left} or {consonants_right_old} != {consonants_right}')
            vowels_left = []
            for vowel in vowels:
                counts = vowel_count[vowel]
                ### print(f'  "{vowel}": {counts}')
                # print(f'  "{vowel}":')
                vowel_i = counts[i]
                # vowel_left = bisect_left(counts, vowel_i + 1)
                try:
                    vowel_left = vowel_first_index[vowel][vowel_i + 1]
                except KeyError:
                    vowel_left = len(word) + 1
                # print(f'    {vowel_i=} [{vowel_left}..]')
                vowels_left.append(vowel_left)
            # print(f'  -> {vowels_left}')
            Left = max(consonants_left, max(vowels_left))
            Right = max(Left, consonants_right)
            # print(f'  => [{Left},{Right}]')
            answer += Right - Left
        
        print(f'{answer=}')
        return answer

# NOTE: Acceptance Rate 40.5% (medium)

# NOTE: Time Limit Exceeded.  Trying another method.

