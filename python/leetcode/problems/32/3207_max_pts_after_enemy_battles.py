class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:

        # deleted entire "munchkin" section because I didn't catch
        # the fact that you can only *attack* unmarked enemies also.

        # we will be attacking only the enemy with minimum energy,
        # and marking all the others starting at the maximum energy end.

        # e.g., for [ A B C D E ] sorted by energy.
        # attack A, losing A power
        # mark BCDE, gaining (sum(enemy) - A) power
        # attack A until we run out of energy

        points = 0
        print(f'{points=} {currentEnergy=}')
        MIN = min(enemyEnergies)
        if currentEnergy < MIN:
            print(f'Cannot attack the least enemy: {currentEnergy=} < {MIN=}')
            print(f'"You get nothing!  You lose!  Good day, sir!"')
            return 0
        
        print(f'\n(1) Attack minimum enemy.')
        print(f'  pew!')
        points += 1
        currentEnergy -= MIN
        print(f'{points=} {currentEnergy=}')

        print(f'\n(2) Siphon from all enemies *except* mister minimum.')
        currentEnergy += sum(enemyEnergies) - MIN
        print(f'{points=} {currentEnergy=}')

        print(f'\n(3) Attack minimum enemy until we run out of power.')
        assert points >= 1
        pews = currentEnergy // MIN
        points += pews
        currentEnergy -= (MIN * pews)
        print(f'  pew! * {pews}')
        print(f'{points=} {currentEnergy=}')
        assert currentEnergy >= 0

        return points

# NOTE: Runtime 444 ms Beats 84.97%
# NOTE: Memory 31.86 MB Beats 31.80%
