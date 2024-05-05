class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        capitals = list([
            1 if ch.isupper() else 0
            for ch in word
        ])
        print(f'{word=} {capitals=}')
        C = sum(capitals)
        if C == 0:
            return True
        if C == len(word):
            return True
        if C == 1:
            if capitals[0] == 1:
                return True
        return False

