class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        (wins, losses) = map(Counter, zip(*matches))
        # print(f'{wins=}')
        # print(f'{losses=}')
        players = set((wins + losses).keys())
        # print(f'{players=}')

        undefeated = [
            P
            for P in players
            if losses[P] == 0
        ]
        undefeated.sort()
        one_loss = [
            P
            for P in players
            if losses[P] == 1
        ]
        one_loss.sort()

        return [undefeated, one_loss]

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (needed to be sorted)
# NOTE: Runtime 283 ms Beats 8.09%
# NOTE: Memory 70.88 MB Beats 5.10%
