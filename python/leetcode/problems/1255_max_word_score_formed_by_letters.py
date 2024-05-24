class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        letter_score = {
            letter: score[index]
            for index, letter in enumerate(list(alphabet))
        }

        def word_score(word: str) -> int:
            retval = 0
            for W in word:
                retval += letter_score[W]
            return retval
        
        def word_remaining_letters(word: str, letters: List[str]) -> List[str]:
            retval = letters.copy()
            print(f'  {word=} {letters=}')
            if len(word) > len(letters):
                print(f'    FAIL ({len(word)}>{len(letters)})')
                return None
            for W in word:
                if W in retval:
                    print(f'    remove {W}')
                    retval.remove(W)
                else:
                    print(f'    FAIL (no {W})')
                    return None
            print(f'  {retval=}')
            return retval
        
        possibles = [
            (0, [], letters)
        ]

        for word in words:
            WS = word_score(word)
            print(f'{word=} score={WS}')
            new_possibles = []
            print(f'  {len(possibles)} possibles:')
            for P in possibles:
                (prior_score, prior_words, prior_letters) = P
                print(f'  {P=}')
                new_letters = word_remaining_letters(word, prior_letters)
                if new_letters is None:
                    print('    will not fit')
                    continue
                
                new_possibles.append(
                    (
                        prior_score + WS,
                        prior_words + [word],
                        new_letters,
                    )
                )
            print(f'    ADD {len(new_possibles)} POSSIBLES')
            possibles.extend(new_possibles)
        
        # print(f'{possibles=}')
        possibles.sort()
        for P in possibles:
            print(f"{P=}")
        return possibles[-1][0]

