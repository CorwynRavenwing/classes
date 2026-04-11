class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        indexesByValue = {}
        for index, value in enumerate(nums):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        print(f'{indexesByValue=}')

        good = set()

        for (value, indexes) in indexesByValue.items():
            adjacent = set(pairwise(indexes))
            # print(f'{adjacent=}')
            pairs = set(itertools.combinations(indexes, 2))
            # print(f'{pairs=}')
            good |= pairs - adjacent

        print(f'{good=}')
        distances = [
            2 * (B - A)
            for (A, B) in good
        ]
        print(f'{distances=}')

        return min(distances, default=-1)

# NOTE: Acceptance Rate 62.0% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 23 ms Beats 30.87%
# NOTE: Memory 21.11 MB Beats 5.03%
