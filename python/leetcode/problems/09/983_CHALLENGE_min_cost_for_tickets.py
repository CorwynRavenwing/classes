class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        (ONE, SEVEN, THIRTY) = costs

        # @cache
        def DP(minDay: int, days: List[int]) -> int:
            print(f'DP({minDay},{days})')
            if not days:
                # no passes, cost no money
                return 0

            today = days[0]

            if minDay > today:
                # skip first day if it's paid for
                return DP(minDay, days[1:])
            
            return min([
                ONE + DP(today + 1, days[1:]),
                SEVEN + DP(today + 7, days[1:]),
                THIRTY + DP(today + 30, days[1:]),
            ])
        
        return DP(0, tuple(days))

# NOTE: Runtime 85 ms Beats 5.09%
# NOTE: Memory 41.78 MB Beats 5.09%

# NOTE: re-ran after online problems:
# NOTE: Runtime 85 ms Beats 5.30%
# NOTE: Memory 41.78 MB Beats 5.33%
# NOTE: ... exact same numbers; slightly better percentages (?)

# NOTE: re-ran for challenge:
# NOTE: Runtime 80 ms Beats 5.67%
# NOTE: Memory 41.36 MB Beats 5.10%
# NOTE: slightly better
