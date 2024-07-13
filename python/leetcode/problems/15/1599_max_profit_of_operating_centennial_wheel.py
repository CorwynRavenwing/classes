class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profitAfterTurnX = []
        running_profit = 0
        profitAfterTurnX.append(running_profit)
        queue = 0
        for i, C in enumerate(customers):
            queue += C
            board = min(4, queue)
            queue -= board
            running_profit += boardingCost * board - runningCost * 1
            # print(f'{i}: +{C=} -{board} Q={queue} ${running_profit}')
            profitAfterTurnX.append(running_profit)
        # print(f'Ran out of customers')
        while queue:
            i += 1
            board = min(4, queue)
            queue -= board
            running_profit += boardingCost * board - runningCost * 1
            # print(f'{i}: -{board} Q={queue} ${running_profit}')
            profitAfterTurnX.append(running_profit)
        # print(f'{profitAfterTurnX=}')
        P = max(profitAfterTurnX)
        if P <= 0:
            return -1
        else:
            return profitAfterTurnX.index(P)
# NOTE: 1335 ms; Beats 56.41%
# NOTE: O(N)
