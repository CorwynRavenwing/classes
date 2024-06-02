class WordDictionary:

    data = None

    def __init__(self):
        # the '#' key contains the 'is-terminal' flag
        self.data = {}

    def addWord(self, word: str) -> None:
        # print(f'insert("{word}"):')
        trie = self.data
        for ch in word:
            # print(f'  "{ch}"')
            trie.setdefault(ch, {})
            trie = trie[ch]
        trie['#'] = True
        # print(f'debug: {self.data}')

    def match_trie_multiple(self, prefix: str) -> List[dict]:
        trie_list = [self.data]
        print(f'match_trie_multiple({prefix}):')
        for ch in prefix:
            new_trie_list = []
            if ch == '.':
                for trie in trie_list:
                    for value, child_trie in trie.items():
                        if value != '#':
                            # print(f' "{ch}" match "{value}"')
                            new_trie_list.append(child_trie)
            else:
                for trie in trie_list:
                    if ch in trie:
                        # print(f'  "{ch}"')
                        new_trie_list.append(trie[ch])
                    else:
                        # print(f'  "{ch}" not found')
                        # drop this one
                        pass
            trie_list = new_trie_list
        return trie_list

    def search(self, word: str) -> bool:
        # print(f'search("{word}"):')
        trie_list = self.match_trie_multiple(word)
        print(f'matched {len(trie_list)} possibilities')
        for trie in trie_list:
            if (trie is not None) and ('#' in trie):
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# NOTE: 1177 ms; Beats 89.12% of users with Python3
