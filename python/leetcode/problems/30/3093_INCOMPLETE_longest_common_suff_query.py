class Solution:

    # create a trie:

    data = None

    def __init__(self):
        # the '#' key contains the 'is-terminal' flag
        self.data = {}

    def insert(self, word: str) -> None:
        # print(f'insert("{word}"):')
        trie = self.data
        for ch in word:
            # print(f'  "{ch}"')
            trie.setdefault(ch, {})
            trie = trie[ch]
        trie['#'] = True
        # print(f'debug: {self.data}')

    def match_trie(self, prefix: str) -> dict:
        # print(f'match_trie({prefix}):')
        trie = self.data
        for ch in prefix:
            if ch in trie:
                # print(f'  "{ch}"')
                trie = trie[ch]
            else:
                # print(f'  "{ch}" NOT FOUND')
                return None
        return trie

    def search(self, word: str) -> bool:
        # print(f'search("{word}"):')
        trie = self.match_trie(word)
        return (trie is not None) and ('#' in trie)

    def startsWith(self, prefix: str) -> bool:
        print(f'startsWith("{prefix}"):')
        trie = self.match_trie(prefix)
        return (trie is not None)

    def topNfromTrie(self, prefix: str, trie: dict, N: int) -> List[str]:
        # print(f'topNfromTrie("{prefix},[trie],{N}"):')
        answer = []
        if (N == 0) or (trie is None):
            return []
        if '#' in trie:
            print(f'  (found "{prefix}")')
            answer.append(prefix)
            N -= 1
        if N == 0:
            return answer
        for ch, subTrie in sorted(trie.items()):
            # print(f'  (loop "{prefix}" + "{ch}")')
            if ch == '#':
                continue
            response = self.topNfromTrie(
                prefix + ch,
                subTrie,
                N
            )
            answer.extend(response)
            if len(response) > N:
                response = response[:N]
            N -= len(response)
            if N == 0:
                return answer
        return answer

    def topNstartingWith(self, prefix: str, N: int) -> List[str]:
        print(f'topNstartingWith("{prefix},{N}"):')
        trie = self.match_trie(prefix)
        return self.topNfromTrie(prefix, trie, N)

    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        for index, word in enumerate(wordsContainer):
            rev = reversed(word)
            # put rev in trie, filed under (1) word length INC (2) index INC
            # store only the index

        answer = [
            # fetch trie value, return index
            None
            for query in wordsQuery
        ]

        return answer

# NOTE: Acceptance Rate 36.9% (HARD)

# NOTE: Incomplete: need to actually perform the given algorithm
