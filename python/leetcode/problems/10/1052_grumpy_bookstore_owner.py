class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        data = list(zip(customers, grumpy))
        # print(f'{data=}')

        happy_customers = [
            (C if (G == 0) else 0)
            for (C, G) in data
        ]
        # print(f'  {happy_customers=}')
        unhappy_customers = [
            (C if (G == 1) else 0)
            for (C, G) in data
        ]
        # print(f'{unhappy_customers=}')
        best_weed = 0
        for i in range(len(unhappy_customers) - minutes + 1):
            frag = unhappy_customers[i:i + minutes]
            weed = sum(frag)
            # print(f'{i=} {frag=} {weed=}')
            best_weed = max(best_weed, weed)
        
        return sum(happy_customers) + best_weed

