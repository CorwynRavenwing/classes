class Solution:
    def countValidWords(self, sentence: str) -> int:

        def is_valid_word(word: str) -> bool:
            alpha = 'abcdefghijklmnopqrstuvwxyz'
            digits = '0123456789'
            hyphen = '-'
            punctuation = '!.,'

            print(f'{word=}')
            for d in digits:
                if d in word:
                    print("  digit")
                    return False
            
            if hyphen in word:
                index = word.index(hyphen)
                if hyphen in word[index + 1:]:
                    print("  two hyphens")
                    return False
                nearby = word[index - 1:index + 2]
                print(f"  hyphen: {nearby=}")
                if len(nearby) != 3:
                    print("    hyphen at beginning or end")
                    return False
                if not nearby[0] in alpha:
                    print(f"    {nearby[0]} not alpha")
                    return False
                if not nearby[-1] in alpha:
                    print(f"    {nearby[-1]} not alpha")
                    return False
                
            for P in punctuation:
                if P in word[:-1]:
                    print("  early punctuation")
                    return False
            
            return True

        sentence = sentence.strip()
        while '  ' in sentence:
            sentence = sentence.replace('  ', ' ')
        words = sentence.split(' ')
        print(f'{words=}')

        valid_words = list([
            word
            for word in words
            if is_valid_word(word)
        ])
        print(f'{valid_words}')
        return len(valid_words)

