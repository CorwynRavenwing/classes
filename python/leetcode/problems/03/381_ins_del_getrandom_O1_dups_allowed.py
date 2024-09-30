class RandomizedCollection:

    # we borrow some code from #380:

    def __init__(self):
        print(f'init()')
        self.List = []
        self.CountByValue = {}
        self.IndexesByValue = {}
        self.Length = 0
        return

    def insert(self, val: int) -> bool:
        print(f'\ninsert({val})')
        already_present = (val in self.CountByValue)
        
        print(f'  yes: {self.Length}')
        self.List.append(val)
        self.IndexesByValue.setdefault(val, [])
        self.IndexesByValue[val].append(self.Length)
        self.CountByValue.setdefault(val, 0)
        self.CountByValue[val] += 1
        self.Length += 1
        # print(f'  DBG {self.List=}')
        # print(f'  DBG {self.CountByValue=}')
        # print(f'  DBG {self.IndexesByValue=}')
        # print(f'  DBG {self.Length=}')
        return not already_present

    def remove(self, val: int) -> bool:
        print(f'\nremove({val})')
        already_present = (val in self.CountByValue)
        if not already_present:
            print(f'  no')
            return False
        
        # print(f'  DBG {self.List=}')
        # print(f'  DBG {self.CountByValue=}')
        # print(f'  DBG {self.IndexesByValue=}')
        # print(f'  DBG {self.Length=}')
        indexVal = self.IndexesByValue[val].pop()   # any index is fine
        assert self.List[indexVal] == val
        self.Length -= 1
        indexEnd = self.Length  # *AFTER* decrementing
        if indexVal == indexEnd:
            print(f'  yes: {val} already at end')
        else:
            endVal = self.List[indexEnd]
            # assert indexEnd in self.IndexesByValue[endVal]  # NOT O(1)
            print(f'  yes: {val}[{indexVal}] <-> {endVal}[{indexEnd}]')
            # swap contents of [indexVal] and [indexEnd] positions
            self.List[indexVal] = endVal    # was self.List[indexEnd]
            self.List[indexEnd] = val       # was self.List[indexVal]
            # print(f'  DBG before {self.IndexesByValue[endVal]=} {endVal=}')
            trash = self.IndexesByValue[endVal].pop()   # last index listed should be right
            # print(f'  DBG middle {self.IndexesByValue[endVal]=} {endVal=} {trash=} {indexEnd=}')
            assert trash == indexEnd                    # verify prior "should" is accurate
            # self.IndexesByValue[endVal].append(indexVal)          # O(1) but WRONG
            bisect.insort(self.IndexesByValue[endVal], indexVal)    # O(logN)
            # print(f'  DBG after  {self.IndexesByValue[endVal]=} {endVal=} {indexVal=}')
        # in either case:
        self.CountByValue[val] -= 1
        if not self.CountByValue[val]:
            del self.CountByValue[val]
            assert self.IndexesByValue[val] == []
            del self.IndexesByValue[val]
        del self.List[-1]
        # print(f'  DBG {self.List=}')
        # print(f'  DBG {self.CountByValue=}')
        # print(f'  DBG {self.IndexesByValue=}')
        # print(f'  DBG {self.Length=}')
        return True

    def getRandom(self) -> int:
        print(f'\ngetRandom()')
        # print(f'  DBG {self.List=}')
        # print(f'  DBG {self.CountByValue=}')
        # print(f'  DBG {self.IndexesByValue=}')
        # print(f'  DBG {self.Length=}')
        index = random.randint(0, self.Length - 1)
        print(f'  {index=}')
        return self.List[index]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# NOTE: re-used most of prior version, with several updates
# NOTE: Runtime 462 ms Beats 7.46%
# NOTE: Memory 69.92 MB Beats 5.01%
