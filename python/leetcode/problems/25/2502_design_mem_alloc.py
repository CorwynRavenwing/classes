class Allocator:

    def __init__(self, n: int):
        # allocated contains {mID: [(startIndex, endIndex), ...], ...}
        # ... merge adjacent blocks within a mID groupd
        self.allocated = {}
        # freeList data contains [(startIndex, endIndex), ...]
        # ... merge adjacent blocks
        self.freeList = [(0, n)]
        return

    def shakeAfter(self, index: int, shakable: List[Tuple[int,int]]) -> None:
        (thisA, thisB) = shakable[index]
        try:
            (nextA, nextB) = shakable[index + 1]
        except IndexError:
            return
        if thisB != nextA:
            return
        # merge them
        shakable[index] = (thisA, nextB)
        _ = shakable.pop(index + 1)
        return
        
    def shakeAt(self, index: int, shakable: List[Tuple[int,int]]) -> None:
        self.shakeAfter(index, shakable)
        if index > 0:
            self.shakeAfter(index - 1, shakable)
        return
    
    def init_mID(self, mID: int) -> None:
        self.allocated.setdefault(mID, [])
        return

    def assign_to_mID(self, mID: int, blockData: Tuple[int,int]) -> None:
        self.init_mID(mID)
        index = bisect_left(self.allocated[mID], blockData)
        self.allocated[mID].insert(index, blockData)
        self.shakeAt(index, self.allocated[mID])
        return

    def assign_to_freelist(self, blockData: Tuple[int,int]) -> None:
        index = bisect_left(self.freeList, blockData)
        self.freeList.insert(index, blockData)
        self.shakeAt(index, self.freeList)
        return

    def allocate(self, size: int, mID: int) -> int:
        print(f'A({size=},{mID=})')
        for blockNum, blockData in enumerate(self.freeList):
            (startIndex, endIndex) = blockData
            blockSize = endIndex - startIndex
            if blockSize < size:
                continue
            blockData = (startIndex + size, endIndex)
            self.freeList[blockNum] = blockData
            print(f'  Found at {startIndex}')
            self.assign_to_mID(mID, (startIndex, startIndex + size))
            return startIndex
        print(f'  Memory not found')
        return -1

    def freeMemory(self, mID: int) -> int:
        print(f'F({mID=})')
        self.init_mID(mID)
        freed = 0
        for blockData in self.allocated[mID]:
            (startIndex, endIndex) = blockData
            blockSize = endIndex - startIndex
            freed += blockSize
            print(f'  freed {blockSize}')
            self.assign_to_freelist(blockData)
        # then, throw away the allocation records:
        self.allocated[mID] = []
        print(f'  >> TOTAL {freed}')
        return freed

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)

# NOTE: Acceptance Rate 48.5% (medium)

# NOTE: Accepted on third Run (argument/use disagreement)
# NOTE: Accepted on first Submit
# NOTE: Runtime 55 ms Beats 50.53%
# NOTE: Memory 18.63 MB Beats 53.39%
