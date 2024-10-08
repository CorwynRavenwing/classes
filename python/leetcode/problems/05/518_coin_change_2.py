class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # we borrow some code from #322:

        possibles = Counter({0: 1})  # the only way to get $ is []
        coins.sort(reverse=True)
        for C in coins:
            print('=' * 60)
            print(f'{C=}')
            frozen_possibles = tuple(possibles.items())
            for (P, count) in frozen_possibles:
                # print('-' * 60)
                print(f'{P} +{C}')
                # print('-' * 60)
                P += C
                while P <= amount:
                    possibles[P] += count
                    # print(P, end=' ')
                    P += C
                # print()
        return possibles[amount]

# NOTE: A faster, non-recursive way of doing this
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 4274 ms Beats 5.00%
# NOTE: Memory 17.97 MB Beats 59.56%
