class MapSum:

    # NOTE: a Trie would be a more robust data structure to use under this,
    # but given the small constraints, we can safely use a simpler version.

    def __init__(self):
        self.Data = defaultdict(int)
        self.PriorKeyVal = defaultdict(int)
        return
    
    def __allPrefixes(self, key: str) -> List[str]:
        return [
            key[:i+1]
            for i in range(len(key))
        ]

    def insert(self, key: str, val: int) -> None:
        PriorValue = self.PriorKeyVal[key]
        self.PriorKeyVal[key] = val
        DeltaValue = val - PriorValue
        for prefix in self.__allPrefixes(key):
            self.Data[prefix] += DeltaValue
        print(f'DEBUG: {self.Data=}')
        return

    def sum(self, prefix: str) -> int:
        return self.Data[prefix]

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 41 ms Beats 22.75%
# NOTE: Memory 16.67 MB Beats 49.04%
