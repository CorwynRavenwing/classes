class Bitset:

    def __init__(self, size: int):
        print(f'INIT({size}):')
        self.size = size
        self.setBits = {}
        self.flipped = False
        self.setCount = 0
        self.unsetCount = size
        print(f'  (count={self.setCount}/{self.unsetCount})')
        # print(f'  {self.toString()}')
        return

    def fix(self, idx: int) -> None:
        if self.flipped:
            if idx in self.setBits:
                print(f'Set bit {idx=} inverted')
                del self.setBits[idx]
                self.setCount += 1
                self.unsetCount -= 1
                print(f'  (count={self.setCount}/{self.unsetCount})')
            else:
                print(f'Ignoring fix({idx}) inverted: set already')
        else:
            if idx not in self.setBits:
                print(f'Set bit {idx=} normally')
                self.setBits[idx] = True
                self.setCount += 1
                self.unsetCount -= 1
                print(f'  (count={self.setCount}/{self.unsetCount})')
            else:
                print(f'Ignoring "fix({idx}) normal": set already')
        # print(f'  {self.toString()}')
        return

    def unfix(self, idx: int) -> None:
        if self.flipped:
            if idx not in self.setBits:
                print(f'Unset bit {idx=} inverted')
                self.setBits[idx] = True
                self.setCount -= 1
                self.unsetCount += 1
                print(f'  (count={self.setCount}/{self.unsetCount})')
            else:
                print(f'Ignoring "unfix({idx}) inverted": unset already')
        else:
            if idx in self.setBits:
                print(f'Unset bit {idx=} normal')
                del self.setBits[idx]
                self.setCount -= 1
                self.unsetCount += 1
                print(f'  (count={self.setCount}/{self.unsetCount})')
            else:
                print(f'Ignoring unfix({idx}) normal: unset already')
        # print(f'  {self.toString()}')
        return

    def flip(self) -> None:
        self.flipped = not self.flipped
        print(f'FLIP() -> {self.flipped}')
        (self.setCount, self.unsetCount) = (self.unsetCount, self.setCount)
        print(f'  (count={self.setCount}/{self.unsetCount})')
        # print(f'  {self.toString()}')
        return

    def all(self) -> bool:
        return (self.unsetCount == 0)

    def one(self) -> bool:
        return (self.setCount != 0)

    def count(self) -> int:
        return self.setCount

    def toString(self) -> str:
        (one, zero) = ('0', '1') if self.flipped else ('1', '0')
        return ''.join([
            one if (i in self.setBits) else zero
            for i in range(self.size)
        ])

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
