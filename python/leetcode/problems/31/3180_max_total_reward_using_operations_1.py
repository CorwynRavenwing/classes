class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:

        # SHORTCUT 1: since we can take values in any order,
        # we are free to sort them if we choose.
        
        # SHORTCUT 2: since we can only take a value when the sum
        # of everything we've taken prior is less than that value,
        # we definitely cannot take a value twice.  Therefore we
        # can also filter our list for duplicates.

        rewardValues = sorted(set(rewardValues))
        # print(f'new {rewardValues=}')

        possibles = {0}     # choose nothing
        print(f'^ {max(possibles)=}')
        for N in rewardValues:
            new_possibles = set()
            for P in possibles:
                if P < N:
                    new_possibles.add(P + N)
            possibles |= new_possibles
            print(f'{N} {max(possibles)=}')

        return max(possibles)

# NOTE: Accepted on first Submit
# NOTE: Runtime 285 ms Beats 88.26%
# NOTE: Memory 17.18 MB Beats 62.99%
