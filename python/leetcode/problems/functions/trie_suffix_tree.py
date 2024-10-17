class Trie:

    data = None

    def __init__(self):
        # the '#' key contains the 'is-terminal' flag
        self.data = {}
    
    def insert(self, word: str) -> None:
        # print(f'insert("{word}"):')
        trie = self.data
        for ch in reversed(word):
            # print(f'  "{ch}"')
            trie.setdefault(ch, {})
            trie = trie[ch]
        trie['#'] = True
        # print(f'debug: {self.data}')
    
    def match_trie(self, suffix: str) -> dict:
        # print(f'match_trie({suffix}):')
        trie = self.data
        for ch in reversed(suffix):
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

    def endsWith(self, suffix: str) -> bool:
        print(f'endsWith("{suffix}"):')
        trie = self.match_trie(suffix)
        return (trie is not None)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.endsWith(suffix)
