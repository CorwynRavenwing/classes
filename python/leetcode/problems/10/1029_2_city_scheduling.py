class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        N = len(costs) // 2
        
        # REV = lambda x: tuple(reversed(tuple(x)))

        SortByPriceDifference = lambda x: (x[0] - x[1])
        # this will put A-is-cheaper first and B-is-cheaper last,
        # in order by magnitude of cheaper-ness

        costs.sort(
            key=SortByPriceDifference
        )
        print(f'{costs=}')

        PICK_0 = lambda x: x[0]
        PICK_1 = lambda x: x[1]

        take_A = costs[:N]
        take_B = costs[N:]

        prices = tuple(map(PICK_0, take_A)) + tuple(map(PICK_1, take_B))
        print(f'{prices=}')

        return sum(prices)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.71 MB Beats 16.57%
