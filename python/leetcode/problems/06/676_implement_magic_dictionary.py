class MagicDictionary:

    # Note: you *must* change one letter, so "abc" does not match "abc"
    # while it does match "abd".  However, if ["abc", "abd"] are in the
    # dictionary, they match both source words plus "abe" and so forth.

    # Therefore, we store the source string for each search string;
    # but if we get two competing sources, we make the source string "*"
    # so that it won't forbid the match.

    def __init__(self):
        self.DataByLength = {}

    def __allPatterns(self, word: str) -> List[str]:
        return [
            word[:i] + '*' + word[i+1:]
            for i in range(len(word))
        ]
    
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            Len = len(word)
            self.DataByLength.setdefault(Len, {})
            for pattern in self.__allPatterns(word):
                self.DataByLength[Len].setdefault(pattern, '')
                if self.DataByLength[Len][pattern]:
                    self.DataByLength[Len][pattern] = '*'
                else:
                    self.DataByLength[Len][pattern] = word
        # print(f'DEBUG: {self.DataByLength}')

    def search(self, searchWord: str) -> bool:
        print(f'search({searchWord}):')
        Len = len(searchWord)
        if Len not in self.DataByLength:
            # there will not be a match
            print(f'  No patterns of length {Len}')
            return False

        for pattern in self.__allPatterns(searchWord):
            # print(f'  Try {pattern=}')
            if pattern not in self.DataByLength[Len]:
                # not a match, but try other patterns
                # print(f'    no')
                continue
            if searchWord == self.DataByLength[Len][pattern]:
                print(f'    exact match of "{searchWord}" does not count')
                continue
            print(f'    YES')
            return True

        print(f'  NO')
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 185 ms Beats 28.64%
# NOTE: Memory 19.62 MB Beats 18.24%
