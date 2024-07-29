# NOTE: no, seriously, that was the name of the challenge given :-/

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:

        REV = lambda x: list(reversed(list(x)))

        def nonIncreasingCountLeft(arr: List[int]) -> List[int]:
            # print(f'NICL({arr}):')
            nonIncreasingOnes = [0] + [
                1 if (A >= B) else 0
                for (A, B) in zip(arr, arr[1:])
            ]
            # print(f'  {nonIncreasingOnes=}')
            # nonIncreasingCount = list(itertools.accumulate(nonIncreasingOnes))
            # nope, hand-roll this because we need 0's to start the count over

            nonIncreasingCount = [None] * len(nonIncreasingOnes)
            nonIncreasingCount[0] = nonIncreasingOnes[0]
            for i in range(1, len(nonIncreasingOnes)):
                nonIncreasingCount[i] = (
                    0
                    if nonIncreasingOnes[i] == 0
                    else
                    nonIncreasingOnes[i] + nonIncreasingCount[i - 1]
                )

            # print(f'  {nonIncreasingCount=}')
            return nonIncreasingCount
        
        def nonDecreasingCountRight(arr: List[int]) -> List[int]:
            return REV(
                nonIncreasingCountLeft(
                    REV(arr)
                )
            )
        
        NICL = nonIncreasingCountLeft(security)
        NDCR = nonDecreasingCountRight(security)
        # print(f'{NICL=}')
        # print(f'{NDCR=}')

        answer = [
            (A >= time) and (B >= time)
            for (A, B) in zip(NICL, NDCR)
        ]
        # print(f'{answer=}')

        return [
            index
            for index, A in enumerate(answer)
            if A
        ]
# NOTE: Runtime 720 ms Beats 15.21%
# NOTE: O(N)
# NOTE: Memory 35.86 MB Beats 55.30%
# NOTE: O(N)
