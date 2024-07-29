class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:

        refills = 0
        waterA = capacityA
        waterB = capacityB
        # print(f'Alice and Bob start with {waterA} and {waterB} in their cans.')
        # print()

        for i in range(len(plants)):
            posA = i
            posB = len(plants) - 1 - i
            needA = plants[posA]
            needB = plants[posB]
            if posA > posB:
                # print(f'Alice has passed Bob.  We are done.')
                break
            if posA < posB:
                if needA > waterA:
                    waterA = capacityA
                    # print(f'Alice fills her can and now has {waterA}')
                    refills += 1
                waterA -= needA
                # print(f'Alice waters #{posA} ({needA}) and now has {waterA}')

                if needB > waterB:
                    waterB = capacityB
                    # print(f'Bob fills his can and now has {waterB}')
                    refills += 1
                waterB -= needB
                # print(f'Bob waters #{posB} ({needB}) and now has {waterB}')
                # print()

            if posA == posB:
                # print(f'Alice and Bob meet at {posA}')
                if waterA >= waterB:
                    # print(f'Alice has more water ({waterA=} >= {waterB})')
                    if needA > waterA:
                        waterA = capacityA
                        # print(f'Alice fills her can and now has {waterA}')
                        refills += 1
                    waterA -= needA
                    # print(f'Alice waters #{posA} ({needA}) and now has {waterA}')
                else:
                    # print(f'Bob has more water ({waterA} < {waterB=})')
                    if needB > waterB:
                        waterB = capacityB
                        # print(f'Bob fills his can and now has {waterB}')
                        refills += 1
                    waterB -= needB
                    # print(f'Bob waters #{posB} ({needB}) and now has {waterB}')
                # print()

        return refills
# NOTE: Runtime 614 ms Beats 20.73%
# NOTE: Memory 31.54 MB Beats 77.44%
