class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:

        mods = [
            N % value
            for N in nums
        ]
        print(f'{mods=}')

        modCounts = Counter(mods)
        for N in range(value):
            modCounts.setdefault(N, 0)
        print(f'{modCounts=}')

        minCount = min(modCounts.values())
        print(f'{minCount=}')

        modsWithMinCount = [
            mod
            for mod, count in modCounts.items()
            if count == minCount
        ]
        print(f'{modsWithMinCount=}')

        minMod = min(modsWithMinCount)
        print(f'{minMod=}')
        
        return (value * minCount) + minMod
# NOTE: Runtime 779 ms Beats 46.89%
# NOTE: Memory 47.17 MB Beats 5.26%
