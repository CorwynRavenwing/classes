class SmallestInfiniteSet:

    def __init__(self):
        self.lowestUnused = 1
        self.addedBack = set()
        return

    def popSmallest(self) -> int:
        if self.addedBack:
            N = min(self.addedBack)
            self.addedBack.remove(N)
            print(f'PS() == {N} from cache')
        else:
            N = self.lowestUnused
            self.lowestUnused += 1
            print(f'PS() == {N} from infinite set')
        return N
        
    def addBack(self, num: int) -> None:
        print(f'AB({num}):')
        if num in self.addedBack:
            print(f'  (already added back)')
            return
        if num >= self.lowestUnused:
            print(f'  (in infinite set [{self.lowestUnused}])')
            return
        print(f'  Returned')
        self.addedBack.add(num)
        return
        
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

# NOTE: Acceptance Rate 71.4% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 53 ms Beats 19.05%
# NOTE: Memory 18.68 MB Beats 13.32%
