class RandomizedSet:

    def __init__(self):
        print(f'init()')
        self.List = []
        self.IndexByValue = {}
        self.Length = 0
        return

    def insert(self, val: int) -> bool:
        print(f'\ninsert({val})')
        if val in self.IndexByValue:
            print(f'  no')
            return False
        
        print(f'  yes: {self.Length}')
        self.List.append(val)
        self.IndexByValue[val] = self.Length
        self.Length += 1
        # print(f'  DBG {self.List=}')
        # print(f'  DBG {self.IndexByValue=}')
        # print(f'  DBG {self.Length=}')
        return True

    def remove(self, val: int) -> bool:
        print(f'\nremove({val})')
        if val not in self.IndexByValue:
            print(f'  no')
            return False
        
        indexVal = self.IndexByValue[val]
        assert self.List[indexVal] == val
        self.Length -= 1
        indexEnd = self.Length  # *AFTER* decrementing
        if indexVal == indexEnd:
            print(f'  yes: {val} already at end')
        else:
            endVal = self.List[indexEnd]
            assert self.IndexByValue[endVal] == indexEnd
            print(f'  yes: {val}[{indexVal}] <-> {endVal}[{indexEnd}]')
            # swap contents of [indexVal] and [indexEnd] positions
            self.List[indexVal] = endVal    # was self.List[indexEnd]
            self.List[indexEnd] = val       # was self.List[indexVal]
            self.IndexByValue[endVal] = indexVal
        # in either case:
        del self.IndexByValue[val]
        del self.List[-1]
        # print(f'  DBG {self.List=}')
        # print(f'  DBG {self.IndexByValue=}')
        # print(f'  DBG {self.Length=}')
        return True

    def getRandom(self) -> int:
        print(f'\ngetRandom()')
        # print(f'  DBG {self.List=}')
        # print(f'  DBG {self.IndexByValue=}')
        # print(f'  DBG {self.Length=}')
        index = random.randint(0, self.Length - 1)
        print(f'  {index=}')
        return self.List[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# NOTE: Runtime 425 ms Beats 29.28%
# NOTE: Memory 64.12 MB Beats 5.84%
