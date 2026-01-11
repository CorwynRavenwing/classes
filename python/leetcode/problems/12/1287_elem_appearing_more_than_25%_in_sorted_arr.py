class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        counts = Counter(arr)
        print(f'{counts=}')
        pairs = list(counts.items())
        BY_SECOND_VALUE_DESC = lambda L: -L[1]
        pairs.sort(key=BY_SECOND_VALUE_DESC)
        print(f'{pairs=}')
        (element, count) = pairs[0]
        return element

# NOTE: Acceptance Rate 61.1% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 11 ms Beats 11.62%
# NOTE: Memory 21.63 MB Beats 5.59%
