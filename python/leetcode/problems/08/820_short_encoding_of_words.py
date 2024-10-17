class Solution:

    # Suffix Trie:
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
        pass

    def endsWith(self, suffix: str) -> bool:
        print(f'endsWith("{suffix}"):')
        trie = self.match_trie(suffix)
        return (trie is not None)
        pass

    def minimumLengthEncoding(self, words: List[str]) -> int:

        words.sort(
            key=len,
            reverse=True
        )
        print(f'sorted {words=}')

        for word in words:
            self.insert(word)
        
        print(f'{self.data=}')

        def check_depth(trie: Dict[str,any], so_far=0) -> int:
            answer = 0
            for (letter, subTrie) in trie.items():
                if letter == '#':
                    continue
                answer += check_depth(subTrie, so_far + 1)
            if not answer:
                # terminal node
                answer = so_far
            return answer

        depth = check_depth(self.data, 1)   # start with 1 for the reference string '#' char

        return depth

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 177 ms Beats 48.83%
# NOTE: Memory 18.65 MB Beats 32.11%
