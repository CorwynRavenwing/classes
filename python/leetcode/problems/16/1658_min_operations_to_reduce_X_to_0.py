class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        partialSums = list(itertools.accumulate(nums))
        # print(f'{[0]} + {partialSums=}')

        PS_indexes = {}
        # add "partial sum" at fictional index "-1" of total 0
        # === sum of "none of these numbers" == 0
        PS_indexes.setdefault(0, [])
        PS_indexes[0].append(-1)
        for i, PS in enumerate(partialSums):
            PS_indexes.setdefault(PS, [])
            PS_indexes[PS].append(i)
        # print(f'{PS_indexes=}')
        keepSum = partialSums[-1] - x
        print(f'{keepSum=} = {partialSums[-1]} - {x}')
        pairs = []
        for LeftSum, LeftIndexes in PS_indexes.items():
            RightSum = LeftSum + keepSum
            if RightSum not in PS_indexes:
                # print(f'{LeftSum} {LeftIndexes}, {RightSum} NOT FOUND')
                continue
            RightIndexes = PS_indexes[RightSum]
            # print(f'{LeftSum} {LeftIndexes}, {RightSum} {RightIndexes}')
            pairs.extend([
                (L, R)
                for L in LeftIndexes
                for R in RightIndexes
                if L <= R
            ])
        # print(f'{pairs=}')
        if not pairs:
            return -1
        keepSizes = [
            R - L
            for (L, R) in pairs
        ]
        # print(f'{keepSizes=}')
        return len(nums) - max(keepSizes)

