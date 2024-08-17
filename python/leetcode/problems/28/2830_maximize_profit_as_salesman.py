class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:

        bestValuePriorToIndex = [0] * (n + 1)
        offers.sort()
        j = 0
        for index in range(n + 1):
            if index > 0:
                print(f'Update {index} from {index-1}')
                bestValuePriorToIndex[index] = max(
                    bestValuePriorToIndex[index],
                    bestValuePriorToIndex[index - 1]
                )
            while j < len(offers):
                (startJ, endJ, goldJ) = offers[j]
                if startJ > index:
                    break
                elif startJ == index:
                    withThisHouse = bestValuePriorToIndex[index] + goldJ
                    print(f'Update {endJ + 1} with ${withThisHouse}')
                    bestValuePriorToIndex[endJ + 1] = max(
                        bestValuePriorToIndex[endJ + 1],
                        withThisHouse
                    )
                # elif startJ < index:
                #     # fall through
                j += 1
        return bestValuePriorToIndex[n]
# NOTE: Accepted on first Submit
# NOTE: Runtime 1372 ms Beats 11.63%
# NOTE: Memory 44.95 MB Beats 46.51%
