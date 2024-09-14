class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        
        @cache
        def drinkA(hour: int) -> int:
            if hour < 0:
                return 0
            # print(f'drinkA({hour})')
            return energyDrinkA[hour] + max(
                drinkA(hour - 1),
                drinkB(hour - 2),
            )

        @cache
        def drinkB(hour: int) -> int:
            if hour < 0:
                return 0
            # print(f'drinkB({hour})')
            return energyDrinkB[hour] + max(
                drinkA(hour - 2),
                drinkB(hour - 1),
            )

        N = len(energyDrinkA)
        return max(
            drinkA(N-1),
            drinkB(N-1),
        )

# NOTE: Accepted on second Submit (first was Output Limit Exceeded)
# NOTE: Runtime 1925 ms Beats 23.20%
# NOTE: Memory 324.92 MB Beats 16.20%
