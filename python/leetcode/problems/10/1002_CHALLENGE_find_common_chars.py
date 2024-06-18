class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        wordLists = list(map(list, words))
        # print(f'{wordLists}')
        answer = []
        pattern = wordLists[0].copy()
        for letter in pattern:
            found_everywhere = all([
                letter in word
                for word in wordLists
            ])
            print(f'{letter}: {found_everywhere}')
            if found_everywhere:
                answer.append(letter)
            for word in wordLists:
                if letter in word:
                    word.remove(letter)
        return answer

