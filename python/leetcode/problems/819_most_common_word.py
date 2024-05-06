from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuation =  list(",.!?';")
        for P in punctuation:
            paragraph = paragraph.replace(P, ' ')
        paragraph = paragraph.replace('  ', ' ')

        words = [
            word.lower()
            for word in paragraph.split(' ')
        ]
        # print(f"{list(words)=}")
        words = [
            word
            for word in words
            if (word) and (word not in banned)
        ]
        # print(f"{list(words)=}")
        wordCounts = Counter(words)
        print(f"{wordCounts=}")
        maxCount = max(wordCounts.values())
        print(f"{maxCount=}")
        maxWord = [
            word
            for word, count in wordCounts.items()
            if count == maxCount
        ]
        print(f"{maxWord=}")
        return maxWord.pop()

