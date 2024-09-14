class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        # we borrow some code from #3254:
        
        powered = [
            1 if (A + 1 == B) else 0
            for (A, B) in pairwise(nums)
        ]
        # print(f'{powered=}')

        POWER = lambda x, y: 1 if (y == 0) else (x + y)

        arraySize = tuple(
            accumulate(
                powered,
                POWER,
                initial=1
            )
        )
        # print(f'{arraySize=}')
        answers = [
            N if (A >= k) else -1
            for (A, N) in zip(arraySize, nums)
        ]
        # print(f'all  {answers=}')
        answers = answers[k-1:]
        # print(f'trim {answers=}')

        return answers

# NOTE: Re-used code from version 1 with minor changes (print less)
# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Limit Exceeded)
# NOTE: Runtime 1413 ms Beats 29.24%
# NOTE: Memory 33.34 MB Beats 27.62%
