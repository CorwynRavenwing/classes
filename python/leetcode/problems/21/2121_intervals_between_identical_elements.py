class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:

        indexesByValue = {}
        for index, value in enumerate(arr):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        # print(f'{indexesByValue=}')
        # print(f'indexesByValue:')
        # for value, indexes in sorted(indexesByValue.items()):
        #     print(f'  {value}: {indexes[:10]}{"..." if len(indexes) > 10 else ""}')
        
        intervalSumByIndex = {}
        for value, allIndexes in indexesByValue.items():
            # print(f'{value}: {allIndexes}')
            leftSize = 0
            leftSum = 0
            rightSize = len(allIndexes[1:])
            rightSum = sum(allIndexes[1:])
            for find_index, thisIndex in enumerate(allIndexes):
                if find_index != 0:
                    # if it *is* zero, we've set this up already
                    leftSize += 1
                    leftSum += allIndexes[find_index - 1]
                    rightSize -= 1
                    rightSum -= thisIndex
                # print(f'  {find_index}: {thisIndex} [{leftSize},{rightSize}]=({leftSum},{rightSum})')
                # we need sum(rightGroup) - (len(rightGroup) * thisIndex)
                # + (len(leftGroup) * thisIndex) - sum(leftGroup)
                # ... the two (thisIndex * N) sections can be merged:
                N_thisIndex = thisIndex * (leftSize - rightSize)
                answer = rightSum - leftSum + N_thisIndex
                intervalSumByIndex[thisIndex] = answer

        answers = [
            intervalSumByIndex[thisIndex]
            for thisIndex in range(len(arr))
        ]

        return answers
# NOTE: Runtime 848 ms Beats 56.41%
# NOTE: O(N)
# NOTE: Memory 56.12 MB Beats 20.94%
# NOTE: O(N)
