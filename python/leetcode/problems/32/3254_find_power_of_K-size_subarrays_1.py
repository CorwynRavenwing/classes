class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        powered = [
            1 if (A + 1 == B) else 0
            for (A, B) in pairwise(nums)
        ]
        print(f'{powered=}')

        POWER = lambda x, y: 1 if (y == 0) else (x + y)

        arraySize = tuple(
            accumulate(
                powered,
                POWER,
                initial=1
            )
        )
        print(f'{arraySize=}')
        answers = [
            N if (A >= k) else -1
            for (A, N) in zip(arraySize, nums)
        ]
        print(f'all  {answers=}')
        answers = answers[k-1:]
        print(f'trim {answers=}')

        return answers

# NOTE: Accepted on first Submit
# NOTE: Runtime 107 ms Beats 77.40%
# NOTE: Memory 16.84 MB Beats 8.28%
