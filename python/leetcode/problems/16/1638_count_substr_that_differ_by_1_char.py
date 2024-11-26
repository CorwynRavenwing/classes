class Solution:

    data = None

    def __init__(self):
        # the '#' key contains the 'is-terminal' flag
        self.data = {}

    # stores count of matches, rather than true/false
    def insert(self, word: str) -> None:
        # print(f'insert("{word}"):')
        trie = self.data
        for ch in word:
            # print(f'  "{ch}"')
            trie.setdefault(ch, {})
            trie = trie[ch]
        trie.setdefault('#', 0)
        trie['#'] += 1
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

    # returns count of matches, rather than true/false
    def search(self, word: str) -> int:
        # print(f'search("{word}"):')
        trie = self.match_trie(word)
        return (
            0
            if (trie is None) or ('#' not in trie)
            else
            trie['#']
        )

    # def startsWith(self, prefix: str) -> bool:
    #     print(f'startsWith("{prefix}"):')
    #     trie = self.match_trie(prefix)
    #     return (trie is not None)

    # def topNfromTrie(self, prefix: str, trie: dict, N: int) -> List[str]:
    #     # print(f'topNfromTrie("{prefix},[trie],{N}"):')
    #     answer = []
    #     if (N == 0) or (trie is None):
    #         return []
    #     if '#' in trie:
    #         print(f'  (found "{prefix}")')
    #         answer.append(prefix)
    #         N -= 1
    #     if N == 0:
    #         return answer
    #     for ch, subTrie in sorted(trie.items()):
    #         # print(f'  (loop "{prefix}" + "{ch}")')
    #         if ch == '#':
    #             continue
    #         response = self.topNfromTrie(
    #             prefix + ch,
    #             subTrie,
    #             N
    #         )
    #         answer.extend(response)
    #         if len(response) > N:
    #             response = response[:N]
    #         N -= len(response)
    #         if N == 0:
    #             return answer
    #     return answer

    # def topNstartingWith(self, prefix: str, N: int) -> List[str]:
    #     print(f'topNstartingWith("{prefix},{N}"):')
    #     trie = self.match_trie(prefix)
    #     return self.topNfromTrie(prefix, trie, N)

    def countSubstrings(self, s: str, t: str) -> int:
        
        all_letters_in_T = ''.join(set(t))
        print(f'{all_letters_in_T=}')

        def all_substrings(s: str) -> List[str]:
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    yield s[i:j]
        
        def all_replacements(s: str, replace: str) -> List[str]:
            for i in range(len(s)):
                left = s[:i]
                right = s[i + 1:]
                for c in replace:
                    yield left + c + right

        for TSS in all_substrings(t):
            # print(f'T: "{TSS}"')
            self.insert(TSS)
        print()

        @cache
        def check_all_replacements(s: str) -> int:
            answer = 0
            for RSS in all_replacements(s, all_letters_in_T):
                if RSS == s:
                    continue
                count = self.search(RSS)
                # if count:
                #     print(f'  {count} "{RSS}"')
                answer += count
            return answer

        answer = 0
        for SSS in all_substrings(s):
            # print(f'S: "{SSS}"')
            count = check_all_replacements(SSS)
            if count:
                print(f'  {count} "{SSS}"')
            answer += count

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 2954 ms Beats 6.10%
# NOTE: Memory 18.05 MB Beats 8.18%
