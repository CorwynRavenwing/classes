class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        indexesByValue = {}
        for index, value in enumerate(nums):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        # print(f'{indexesByValue=}')
        # indexes listed will be in order, because of the enumerate above

        arr = [None] * len(nums)
        for value, indexList in indexesByValue.items():
            print(f'Checking {value=}:')
            partialSums = (0,) + tuple(accumulate(indexList))
            # print(f'  {indexList=}')
            # print(f'  {partialSums=}')
            listLength = len(indexList)
            # print(f'  {listLength=}')
            for i, numIndex in enumerate(indexList):
                # divide indexList into two parts:
                # left half, in list prior to numIndex, will be LT numIndex
                # right half, in list after numIndex, will be GT numIndex
                # (we skip numIndex itself)
                # (none will be equal b/c these are indexes of different 'nums' values)

                # we seek sum( abs(i - j) )
                # where i == numIndex and j == each other value in indexList
                # for left half, j < numIndex so abs(numIndex - j) === numIndex - j
                # for right half, j > numIndex so abs(numIndex - j) === j - numIndex

                # therefore the sum we seek ===
                # rightSum - leftSum + numIndex * (leftLength - rightLength)
                leftSum = partialSums[i] - partialSums[0]
                rightSum = partialSums[listLength] - partialSums[i + 1]
                leftLength = i
                rightLength = listLength - i - 1
                # print(f'    {leftSum=} = {partialSums[i]}-{partialSums[0]}')
                # print(f'    {rightSum=} = {partialSums[listLength]}-{partialSums[i + 1]}')
                # print(f'    {leftLength=} = {i}')
                # print(f'    {rightLength=} = {listLength - i - 1}')
                nSums = numIndex * (leftLength - rightLength)
                # print(f'    {nSums=} = {numIndex} * ({leftLength - rightLength})')
                answer = sum([
                    rightSum,
                    -leftSum,
                    nSums
                ])
                # print(f'  Set [{i}] {numIndex} = {answer}')
                assert arr[numIndex] is None
                arr[numIndex] = answer

        return arr
# NOTE: Runtime 652 ms Beats 21.55%
# NOTE: Memory 49.04 MB Beats 67.07%
