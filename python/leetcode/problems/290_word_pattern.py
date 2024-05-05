class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letters = list(pattern)
        words = s.split(' ')
        letter_list = tuple(set(letters))
        # print(f"{letters} {letter_list} {words}")
        if len(letters) != len(words):
            # print("different lengths")
            return False
        seen_words = []
        for letter in letter_list:
            print(f"  {letter=}")
            start = 0
            pos = 0
            word = ''
            while pos != -1:
                try:
                    pos = letters.index(letter, start)
                except ValueError:
                    pos = -1
                    continue
                new_word = words[pos]
                print(f"    {new_word}")
                if word == '':
                    word = new_word
                    if word in seen_words:
                        # print(f"    DUP {word}")
                        return False
                    else:
                        seen_words.append(word)
                if word != new_word:
                    # print(f"    {start=} {pos=} '{word}' '{new_word}'")
                    return False
                start = pos + 1
        return True

