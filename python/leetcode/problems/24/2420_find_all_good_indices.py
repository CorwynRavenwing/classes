class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        
        # we borrow some code from #2100:

        REV = lambda x: list(reversed(list(x)))

        def nonIncreasingCountLeft(arr: List[int]) -> List[int]:
            # print(f'NICL({arr}):')
            nonIncreasingOnes = [
                1 if (A >= B) else 0
                for (A, B) in zip([float('inf')] + arr, arr)
            ]
            # print(f'  {nonIncreasingOnes=}')
            # nonIncreasingCount = list(itertools.accumulate(nonIncreasingOnes))
            # nope, hand-roll this because we need 0's to start the count over

            nonIncreasingCount = [None] * len(nonIncreasingOnes)
            nonIncreasingCount[0] = nonIncreasingOnes[0]
            for i in range(1, len(nonIncreasingOnes)):
                nonIncreasingCount[i] = (
                    1   # any single value is non-increasing
                    if nonIncreasingOnes[i] == 0
                    else
                    nonIncreasingOnes[i] + nonIncreasingCount[i - 1]
                )

            # print(f'  {nonIncreasingCount=}')
            nonIncreasingCount = [0] + nonIncreasingCount[:-1]  # 0 on front, delete last
            return nonIncreasingCount

        def nonDecreasingCountRight(arr: List[int]) -> List[int]:
            return REV(
                nonIncreasingCountLeft(
                    REV(arr)
                )
            )

        NICL = nonIncreasingCountLeft(nums)
        NDCR = nonDecreasingCountRight(nums)
        print(f'{NICL=}')
        print(f'{NDCR=}')

        answer = [
            (A >= k) and (B >= k)
            for (A, B) in zip(NICL, NDCR)
        ]
        # print(f'{answer=}')

        return [
            index
            for index, A in enumerate(answer)
            if A
        ]

