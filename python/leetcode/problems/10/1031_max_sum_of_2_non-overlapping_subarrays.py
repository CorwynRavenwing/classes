class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        ACC = lambda x: (0,) + tuple(accumulate(x))
        REV = lambda x: tuple(reversed(tuple(x)))
        MAX = lambda x: tuple(accumulate(tuple(x), max))

        partialSums = ACC(nums)

        INDEXES = lambda length: tuple([
            i + length - 1
            for i in range(len(partialSums) - length)
        ])

        SUMS = lambda length: tuple([
            partialSums[B + 1] - partialSums[A]
            for (A, B) in enumerate(INDEXES(length))
        ])

        firstIndexes = INDEXES(firstLen)
        secondIndexes = INDEXES(secondLen)
        print(f'{firstIndexes=}')
        print(f'{secondIndexes=}')
        firstSums = SUMS(firstLen)
        secondSums = SUMS(secondLen)
        print(f'{firstSums=}')
        print(f'{secondSums=}')
        firstMax = MAX(firstSums)
        secondMax = MAX(secondSums)
        print(f'{firstMax=}')
        print(f'{secondMax=}')

        def getAnswers(maxA: List[int], indexA: List[int], sumB: List[int]) -> List[int]:
            print(f'getAnswers({maxA},{indexA},{sumB})')

            PICKSUM = lambda i: (sumB[i + 1] if i + 1 < len(sumB) else float('-inf'))

            sumB_RightOfA = tuple(map(PICKSUM, indexA))
            print(f'  {sumB_RightOfA=}')

            answer = tuple([
                A + B
                for (A, B) in zip(maxA, sumB_RightOfA)
            ])
            print(f'  {answer=}')
            return answer

        answersAB = getAnswers(firstMax, firstIndexes, secondSums)
        answersBA = getAnswers(secondMax, secondIndexes, firstSums)
        print(f'{answersAB=}')
        print(f'{answersBA=}')

        return max(answersAB + answersBA)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 15 ms Beats 34.33%
# NOTE: Memory 17.46 MB Beats 6.65%
