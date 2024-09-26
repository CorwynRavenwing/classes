class Solution:

    Trie = {}

    def clearTrie(self) -> None:
        self.Trie = {}

    def insertTrie(self, word: str) -> None:
        # print(f'insertTrie({word})')
        # print(f'DEBUG[^]: {self.Trie=}')
        node = self.Trie
        # there is no Trie['#']: if it existed, it would count empty strings
        for char in word:
            # print(f'  {char=}')
            node.setdefault(char, {})   # create new Trie for this character
            node = node[char]           # move into new Trie
            node.setdefault('#', 0)     # create counter on NEW Trie
            node['#'] += 1              # increment counter
            # print(f'DEBUG[{char}]: {self.Trie=}')
        return

    def sumTrie(self, word: str) -> int:
        # print(f'sumTrie({word})')
        node = self.Trie
        answer = 0
        for char in word:
            node = node[char]
            answer += node['#']
        return answer

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.clearTrie()

        for W in words:
            self.insertTrie(W)
        
        answer = [
            self.sumTrie(W)
            for W in words
        ]
        return answer

# NOTE: The "Trie" version: excellent
# NOTE: Runtime 1391 ms Beats 91.04%
# NOTE: Memory 212.59 MB Beats 92.41%
