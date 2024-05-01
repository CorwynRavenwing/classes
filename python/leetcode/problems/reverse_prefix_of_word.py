class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        index = word.index(ch)
        firsthalf = word[:index+1]
        secondhalf = word[index+1:]
        fh_rev_list = reversed(firsthalf)
        fh_reversed = ''.join(fh_rev_list)

        return fh_reversed + secondhalf

