class Solution:
    def longestWord(self, words: List[str]) -> str:

        Prefix = {
            word: word[:-1]
            for word in words
        }
        print(f'{Prefix=}')

        Suffixes = {
            P: {
                word
                for word, prefix in Prefix.items()
                if P == prefix
            }
            for P in set(Prefix.values())
        }
        print(f'{Suffixes=}')

        queue = {''}
        while queue:
            print(f'{queue=}')
            newQ = set()
            for prefix in queue:
                if prefix in Suffixes:
                    for word in Suffixes[prefix]:
                        newQ.add(word)
            if not newQ:
                return min(queue)
            queue = newQ

        return 'NOPE'

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 214 ms Beats 5.10%
# NOTE: Memory 17.59 MB Beats 39.53%
