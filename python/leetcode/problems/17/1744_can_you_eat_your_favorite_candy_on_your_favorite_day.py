class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:

        candySums = list(itertools.accumulate(candiesCount))

        def minDay(candyType: int, dailyCap: int) -> int:
            # print(f'minDay({candyType},{dailyCap})')
            # print(f'  frag={candiesCount[:candyType]}')
            # print(f'  sum={sum(candiesCount[:candyType])}')
            # print(f'  div={sum(candiesCount[:candyType]) // dailyCap}')
            # first candy, dailyCap per day
            allPriorCandy = (
                candySums[candyType - 1]
                if candyType > 0
                else 0
            )
            return allPriorCandy // dailyCap

        def maxDay(candyType: int) -> int:
            # print(f'maxDay({candyType})')
            # print(f'  frag={candiesCount[:candyType + 1]}')
            # print(f'  sum={sum(candiesCount[:candyType + 1])}')
            # last candy, one per day
            allPriorCandyPlusThisOne = candySums[candyType]
            return allPriorCandyPlusThisOne - 1
            # "-1" == "saving one to happen on the day in question"

        return [
            minDay(typeI, dailyCapI) <= dayI <= maxDay(typeI)
            for (typeI, dayI, dailyCapI) in queries
        ]
# NOTE: Runtime 1114 ms; Beats 93.46%
# NOTE: Memory 75.10 MB; Beats 21.50%
