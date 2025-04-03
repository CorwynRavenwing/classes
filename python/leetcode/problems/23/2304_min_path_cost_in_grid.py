class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:

        M = len(grid)
        N = len(grid[0])

        # for each level above the lowest, in reverse order,
        # add the best possible cost from the next layer down
        # plus the cost of getting to that cell. 

        for X in reversed(range(M - 1)):
            print(f'{X=}')
            for Y1 in range(N):
                value1 = grid[X][Y1]
                # print(f'  {Y1=} {value1=}')
                costArray = moveCost[value1]
                prices = []
                for Y2 in range(N):
                    value2 = grid[X + 1][Y2]
                    cost = costArray[Y2]
                    # print(f'    {Y2=} {cost=} {value2=}')
                    price = cost + value2
                    # print(f'      {price=}')
                    prices.append(price)
                # print(f'  {prices=}')
                price = min(prices)
                print(f'  {value1} + {price} -> {value1 + price}')
                grid[X][Y1] += price
        
        return min(grid[0])

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 129 ms Beats 89.81%
# NOTE: Memory 24.35 MB Beats 18.87%
