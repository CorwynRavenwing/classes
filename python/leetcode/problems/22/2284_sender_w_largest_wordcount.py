class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        
        wordcounts = Counter()
        for Sender, Message in zip(senders, messages):
            words = Message.split(' ')
            count = len(words)
            print(f'[{Sender}]: {count} "{Message}"')
            wordcounts[Sender] += count
        print(f'{wordcounts=}')

        max_wordcount = max(wordcounts.values())
        print(f'{max_wordcount=}')
        users = [
            Sender
            for Sender, count in wordcounts.items()
            if count == max_wordcount
        ]
        print(f'{users=}')

        return max(users)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 115 ms Beats 5.54%
# NOTE: Memory 25.11 MB Beats 8.65%
