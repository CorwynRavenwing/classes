class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:

        indexesByValue = {}
        for index, value in enumerate(nums):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        # print(f'{indexesByValue=}')

        gapsByValue = {}
        for value, indexList in indexesByValue.items():
            if len(indexList) == 1:
                # one entry === "gap" wraps around the whole array
                gapsByValue[value] = [len(nums)]
                continue
            gapsByValue[value] = [
                B - A
                for A, B in itertools.pairwise(indexList)
            ] + [
                # wrap-around gap between last and first
                (indexList[0] - indexList[-1]) % len(nums)
            ]
        # print(f'{gapsByValue=}')

        maxTimeByValue = {
            value: max(gapList) // 2
            for value, gapList in gapsByValue.items()
        }
        # print(f'{maxTimeByValue=}')
        
        return min(
            maxTimeByValue.values()
        )
# NOTE: Runtime 677 ms Beats 60.64%
# NOTE: Memory 69.61 MB Beats 5.32%
