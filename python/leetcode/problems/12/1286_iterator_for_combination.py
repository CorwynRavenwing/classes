class CombinationIterator:

    def bump(self, whichIndex: int):
        print(f'bump({whichIndex})')
        if whichIndex < 0:
            self.indexes = None
        if self.indexes is None:
            print(f'  bumped: stop')
            return
        
        # the actual bump:
        self.indexes[whichIndex] += 1
        # delete any indexes after the one we bumped:
        self.indexes = self.indexes[:whichIndex + 1]

        # fill in the missing other indexes:
        while len(self.indexes) < self.length:
            lastIndex = self.indexes[-1]
            self.indexes.append(
                lastIndex + 1
            )
        
        # verify the indexes haven't overflowed:
        lastIndex = self.indexes[-1]
        if lastIndex >= len(self.chars):
            print(f'  bumped: roll-over')
            self.bump(whichIndex - 1)
            return
        
        print(f'  bumped: {self.indexes=}')
        return
    
    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.length = combinationLength
        self.indexes = [-1]
        self.bump(0)

    def next(self) -> str:
        answer = [
            self.chars[i]
            for i in self.indexes
        ]
        self.bump(self.length - 1)
        return ''.join(answer)

    def hasNext(self) -> bool:
        return (self.indexes is not None)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# NOTE: Accepted on second Run (first was fencepost error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 15 ms Beats 12.39%
# NOTE: Memory 19.34 MB Beats 38.25%
