class LUPrefix:

    def __init__(self, n: int):
        self.highest = 0
        self.uploaded = set()
        # throw N away
        return
    
    def __clean(self) -> None:
        print(f'c()')
        while (self.highest + 1) in self.uploaded:
            self.highest += 1
            print(f'  -> {self.highest}')
        return

    def upload(self, video: int) -> None:
        print(f'U({video}):')
        self.uploaded.add(video)
        self.__clean()
        return

    def longest(self) -> int:
        print(f'L():')
        self.__clean()
        return self.highest

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()

# NOTE: Acceptance Rate 56.3% (medium)

# NOTE: Accepted on second Run (logic error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 374 ms Beats 8.11%
# NOTE: Memory 78.06 MB Beats 21.62%
