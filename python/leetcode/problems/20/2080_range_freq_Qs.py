class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.indexesForValue = {}
        for i, value in enumerate(arr):
            self.indexesForValue.setdefault(value, [])
            self.indexesForValue[value].append(i)
        return

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.indexesForValue:
            print(f'NO ENTRIES FOR {value=}')
            return 0
        indexes = self.indexesForValue[value]
        # print(f'{indexes=}')
        findLeft = bisect_left(indexes, left)
        if findLeft >= len(indexes):
            print(f'"left" is off the right end of the array')
            return 0
        # print(f'{left=} {findLeft=}', end='')
        L = indexes[findLeft]
        # print(f' ... {L=}')
        findRight = bisect_right(indexes, right)
        if findRight > 0:
            findRight -= 1
        # print(f'{right=} {findRight=}', end='')
        R = indexes[findRight]
        # print(f' ... {R=}')
        if left <= L <= R <= right:
            # how many items are in list between these indexes (inclusive)?
            return findRight - findLeft + 1
        else:
            print(f'Condition {left} <= {L} <= {R} <= {right} DOES NOT hold')
            return 0

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

# NOTE: Runtime 1013 ms Beats 51.67%
# NOTE: O(1)
# NOTE: Memory 55.48 MB Beats 45.45%
# NOTE: O(N)
