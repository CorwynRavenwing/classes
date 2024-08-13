class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        @cache
        def schemesAvailable(robbers: int, profitRequired: int, crimeIndex: int, depth=0) -> int:
            # margin = '  ' * depth
            # We are at crime #crimeIndex, and can choose to take it or not.
            # Choice 0a: we are out of crimes
            if crimeIndex >= len(group):
                # print(f'  Out of crimes {crimeIndex=}')
                return 0
            # Choice 0b: we are out of robbers
            if robbers <= 0:
                # print(f'{margin}  Out of {robbers=}')
                return 0
            # print(f'{margin}schemesAvailable({robbers},{profitRequired},{crimeIndex})')
            # Choice 1: don't take it
            dont_take = schemesAvailable(
                robbers,
                profitRequired,
                crimeIndex + 1,
                depth + 1
            )
            # print(f'{margin}  {dont_take=}')
            # Choice 2: take this one, if we can
            if group[crimeIndex] > robbers:
                # print(f'{margin}  cannot take crime {crimeIndex}:')
                # print(f'{margin}    out of {robbers=} {group[crimeIndex]}')
                do_take = 0
            else:
                newProfitRequired = profitRequired - profit[crimeIndex]
                newProfitRequired = max(0, newProfitRequired)
                do_take = (
                    (
                        (
                            # THIS SCHEME ITSELF
                            1
                            # only if we already have enough profit
                            if newProfitRequired <= 0
                            else 0
                        )
                    ) + (
                        schemesAvailable(
                            robbers - group[crimeIndex],
                            newProfitRequired,
                            crimeIndex + 1,
                            depth + 1
                        )
                    )
                )
                # print(f'{margin}  {do_take=}')
            # print(f'{margin}  Total={dont_take+do_take}')
            return dont_take + do_take
        
        mod = 10 ** 9 + 7
        answer = schemesAvailable(n, minProfit, 0)
        if minProfit == 0:
            # count the "pirates who don't do anything" scheme
            answer += 1
        return answer % mod
# NOTE: Runtime 2722 ms Beats 48.20%
# NOTE: Memory 722.34 MB Beats 5.04%
