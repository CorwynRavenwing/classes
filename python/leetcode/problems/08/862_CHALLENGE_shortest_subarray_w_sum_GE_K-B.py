class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        if max(nums) >= k:
            return 1
        
        # if len(nums) >= 10:
        #     return -99999
        
        partialSums = (0,) + tuple(accumulate(nums))
        print(f'{partialSums=}')
        max_sum = max(partialSums)
        print(f'Max Partial Sum: {max_sum}')

        INF = 10 ** 10

        answers = [None] * len(nums)
        for i, N in enumerate(nums):
            if N < 0:
                answers[i] = INF
                print(f'{i}: {N=} SKIP')
                continue
            bottom = partialSums[i]
            # if bottom < 0:
            #     answers[i] = INF
            #     print(f'{i}: {bottom=} SKIP')
            #     continue
            min_top = bottom + k
            print(f'{i}: {bottom=} {min_top=}')
            if min_top > max_sum:
                answers[i] = INF
                print(f'  INF A')
                continue
            for j, top in enumerate(partialSums[i + 1:]):
                if top >= min_top:
                    length = j + 1
                    answers[i] = length
                    print(f'  {j=} {top=} {length=}')
                    break
            if answers[i] is None:
                answers[i] = INF
                print(f'  INF B')

        answer = min(answers)
        
        return (
            answer
            if answer < INF
            else -1
        )
        
# NOTE: Acceptance Rate 27.0% (HARD)
# NOTE: Another version, which also times out for large inputs
