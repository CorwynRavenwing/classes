class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # reuse some code from #140, which I answered first
        
        possibles = [
            ([], s)
        ]

        string_left_cache = []

        while possibles:
            P = possibles.pop()
             # print(f'{P=}')
            (prior_words, string_left) = P
            if not string_left:
                 # print(f'  FOUND {prior_words}')
                return True
            if string_left in string_left_cache:
                # we're already checking a set of words
                # which consume the same left portion
                # and leave this same right-hand portion over.
                # if that one works, this one will work,
                # and vice versa.  Therefore we stop thinking
                # about this possibility.
                # print(f'CACHE HIT {string_left}')
                # print(f'CACHE HIT L={len(string_left)}')
                continue
            else:
                string_left_cache.append(string_left)
            for word in wordDict:
                 # print(f'  {word=}')
                if string_left.startswith(word):
                     # print(f'    match!')
                    new_words = prior_words + [word]
                    new_string = string_left[len(word):]
                     # print(f'    {word} + {new_string}')
                    possibles.append(
                        (new_words, new_string)
                    )
        return False

