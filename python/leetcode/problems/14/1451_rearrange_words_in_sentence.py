class Solution:
    def arrangeWords(self, text: str) -> str:
        
        words = text.lower().split(' ')
        print(f'{words=}')

        BY_LENGTH = lambda x: len(x)
        words.sort(key=BY_LENGTH)
        print(f'{words=}')

        words[0] = words[0].title()
        print(f'{words=}')

        return ' '.join(words)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 15 ms Beats 38.76%
# NOTE: Memory 18.61 MB Beats 74.57%
