class AllOne:

    DEBUG = False

    def __init__(self):
        self.CountForKey = {}       # dict of key -> count
        self.KeysForCount = {}      # dict of count -> set of keys
        self.CountForCount = {}     # dict of count -> how many keys have that count
        self.CountList = []         # dict of all existing C4C values, in order
        self.MaxCount = None        # CountList[0]
        self.MinCount = None        # CountList[-1]
        return
    
    def changeCountCount(self, value: int, delta: int) -> None:
        if self.DEBUG: print(f'cCC({value},{delta})')
        if value == 0:
            if self.DEBUG: print(f'  CC: ignore changes to "0"')
            return
        if value not in self.CountForCount:
            if self.DEBUG: print(f'  CC: new {value=}: insert')
            assert delta > 0
            self.CountForCount.setdefault(value, 0)
            countWasZero = True
        else:
            countWasZero = False

        oldCountCount = self.CountForCount[value]
        newCountCount = oldCountCount + delta
        if self.DEBUG: print(f'  CC: Change count for {value=} from {oldCountCount} to {newCountCount}')

        if newCountCount:
            self.CountForCount[value] = newCountCount
            countWasDeleted = False
        else:
            del self.CountForCount[value]
            countWasDeleted = True
        if self.DEBUG: print(f'  CC: {self.CountForCount=}')

        if countWasZero:
            index = bisect_left(self.CountList, value)
            if self.DEBUG: print(f'  CC: count was zero: insert new {value=} at {index=}')
            if len(self.CountList) == 0:
                # zero before insert === 1 after insert
                self.MinCount = value
                self.MaxCount = value
                if self.DEBUG: print(f'    CC: list length 1: new minimum {self.MinCount}')
                if self.DEBUG: print(f'    CC: list length 1: new maximum {self.MaxCount}')
            elif index == 0:
                if self.DEBUG: print(f'    CC: index zero: new minimum')
                self.MinCount = value
            elif index == len(self.CountList):
                if self.DEBUG: print(f'    CC: index EOL: new maximum')
                self.MaxCount = value
            self.CountList.insert(index, value)
            if self.DEBUG: print(f'  CC: {self.MinCount=} {self.CountList=} {self.MaxCount=}')
        elif countWasDeleted:
            index = bisect_left(self.CountList, value)
            assert 0 <= index < len(self.CountList)
            if self.DEBUG: print(f'  CC: count is now zero: delete old {value=} at {index=}')
            del self.CountList[index]
            if len(self.CountList) == 0:
                self.MinCount = None
                self.MaxCount = None
                if self.DEBUG: print(f'    CC: list empty: new minimum {self.MinCount}')
                if self.DEBUG: print(f'    CC: list empty: new maximum {self.MaxCount}')
            elif index == 0:
                self.MinCount = self.CountList[0]
                if self.DEBUG: print(f'    CC: index zero: new minimum {self.MinCount}')
            elif index == len(self.CountList):
                # after deletion, "last member" becomes "off right end by 1"
                self.MaxCount = self.CountList[-1]
                if self.DEBUG: print(f'    CC: index EOL: new maximum {self.MaxCount}')
            if self.DEBUG: print(f'  CC: {self.MinCount=} {self.CountList=} {self.MaxCount=}')
        return

    def changeKeyCount(self, key: str, delta: int) -> None:
        if self.DEBUG: print(f'cKC({key},{delta})')
        if key not in self.CountForKey:
            if self.DEBUG: print(f'  KC: new {key=}: insert')
            assert delta > 0
            self.CountForKey.setdefault(key, 0)
        
        oldKeyCount = self.CountForKey[key]
        newKeyCount = oldKeyCount + delta
        if self.DEBUG: print(f'  KC: Change count for {key=} from {oldKeyCount} to {newKeyCount}')
        
        if newKeyCount:
            self.CountForKey[key] = newKeyCount
        else:
            del self.CountForKey[key]
        if self.DEBUG: print(f'  KC: {self.CountForKey=}')
        
        if oldKeyCount:
            self.KeysForCount[oldKeyCount].remove(key)
        if newKeyCount:
            self.KeysForCount.setdefault(newKeyCount, set())
            self.KeysForCount[newKeyCount].add(key)
        if self.DEBUG: print(f'  KC: {self.KeysForCount=}')
        
        self.changeCountCount(newKeyCount, +1)  # add new first
        self.changeCountCount(oldKeyCount, -1)  # then delete old
        
        return

    def inc(self, key: str) -> None:
        return self.changeKeyCount(key, +1)

    def dec(self, key: str) -> None:
        return self.changeKeyCount(key, -1)
    
    def __getRandomStringFromSet(self, S: Set[str]) -> str:
        for member in S:
            return member
        return ""

    def getMaxKey(self) -> str:
        if self.MaxCount is None:
            return ""
        matches = self.KeysForCount[self.MaxCount]
        return self.__getRandomStringFromSet(matches)

    def getMinKey(self) -> str:
        if self.MinCount is None:
            return ""
        matches = self.KeysForCount[self.MinCount]
        return self.__getRandomStringFromSet(matches)

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# NOTE: Difficulty = HARD
# NOTE: Acceptance Rate = 37.3%
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 181 ms Beats 21.02%
# NOTE: Memory 35.67 MB Beats 6.23%
