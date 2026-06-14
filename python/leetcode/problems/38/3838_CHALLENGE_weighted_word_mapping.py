class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        letter_map = lambda letter: alphabet.index(letter)
        letter_weight = lambda letter: weights[ letter_map(letter) ]

        alphabet_R = tuple(reversed(alphabet))
        letter_R = lambda value: alphabet_R[ value % 26 ]

        word_letter_weights = [
            [
                letter_weight(letter)
                for letter in word
            ]
            for word in words
        ]
        print(f'{word_letter_weights=}')

        word_weights = tuple(map(sum, word_letter_weights))
        print(f'{word_weights=}')

        answer = [
            letter_R(word_weight)
            for word_weight in word_weights
        ]
        # print(f'{answer=}')

        return ''.join(answer)

# NOTE: Acceptance Rate 86.3% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 23 ms Beats 5.89%
# NOTE: Memory 19.50 MB Beats 8.53%
