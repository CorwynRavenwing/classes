class Solution:
    def minimumCoins(self, prices: List[int]) -> int:

        @cache
        def costOfFruitIthroughN(i: int) -> int:
            # print(f'COFITN({i})')
            if i == len(prices):
                # print(f'  zero: i == len(prices)')
                return 0
            if i >= len(prices):
                # print(f'  inf: i > len(prices)')
                return 999999
            L = len(prices)
            free = i+i+1
            minJ = i+1
            maxJ = min(L,free+1)    # +1 = pay for the next after all the free ones
            # print(f'checking range({minJ}, min({L},{free})+1)={list(range(minJ, maxJ+1))}')
            free_fruit = [
                costOfFruitIthroughN(j)
                for j in range(minJ, maxJ+1)
            ]
            print(f'  [{i}] ${prices[i]} + min({sorted(free_fruit)[:3]}...)')
            return prices[i] + min(free_fruit, default=0)
        
        answer = costOfFruitIthroughN(0)
        # for i in range(len(prices)):
        #     # print(f'[{i}]: {costOfFruitIthroughN(i)}')
        return answer
# NOTE: Runtime 426 ms Beats 55.87%
# NOTE: Memory 18.69 MB Beats 40.08%
