class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:

        n = len(skill)
        m = len(mana)
        
        f = [0] * n
        for potion, mana_value in enumerate(mana):
            startTime = f[0]
            # print(f'{startTime}s {potion}: {f=}')
            for wizard, skill_value in enumerate(skill):
                if wizard == 0:
                    continue
                startTime = max(
                    startTime + skill[wizard - 1] * mana_value,
                    f[wizard]
                )
                # print(f'  {wizard=} {skill_value=} {startTime=}')
            f[n - 1] = startTime + skill[n - 1] * mana_value
            for i in reversed(range(n - 1)):
                f[i] = f[i + 1] - skill[i + 1] * mana_value

        startTime = f[0]
        # print(f'{startTime}s (done): {f=}')

        return f[-1]

# NOTE: Acceptance Rate 39.4% (medium)

# NOTE: Accepted on second Run (variable-name typo)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 14251 ms Beats 11.54%
# NOTE: Memory 18.54 MB Beats 71.15%
