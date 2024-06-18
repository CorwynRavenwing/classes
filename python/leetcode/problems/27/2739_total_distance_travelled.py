class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:

        distance = 0
        while mainTank:
            print(f'{distance=} {mainTank=} {additionalTank=}')
            if mainTank >= 5:
                mainTank -= 5
                distance += 5 * 10
                if additionalTank:
                    additionalTank -= 1
                    mainTank += 1
            else:
                distance += mainTank * 10
                mainTank -= mainTank
                # additionalTank doesn't fire
        print(f'{distance=} {mainTank=} {additionalTank=}')
        return distance

