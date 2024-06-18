class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        possibles = [
            ([], s)
        ]

        answers = []
        while possibles:
            P = possibles.pop()
            print(f'{P=}')
            (prior_words, string_left) = P
            if not string_left:
                print(f'  FOUND {prior_words}')
                answers.append(
                    ' '.join(prior_words)
                )
                continue
            for word in wordDict:
                print(f'  {word=}')
                if string_left.startswith(word):
                    print(f'    match!')
                    new_words = prior_words + [word]
                    new_string = string_left[len(word):]
                    print(f'    {word} + {new_string}')
                    possibles.append(
                        (new_words, new_string)
                    )
        print(f'{answers=}')
        return answers

