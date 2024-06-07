class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        dictionary.sort()   # puts shorter words before longer, matching ones
        words = sentence.split()
        new_words = []
        for word in words:
            found = False
            for D in dictionary:
                if word.startswith(D):
                    print(f'"{word}" starts with "{D}"')
                    found = True
                    new_words.append(D)
                    break
            if not found:
                print(f'"{word}" not in dictionary')
                new_words.append(word)
        return ' '.join(new_words)

