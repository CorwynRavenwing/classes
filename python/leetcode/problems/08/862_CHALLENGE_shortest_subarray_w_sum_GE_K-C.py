class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        if max(nums) >= k:
            return 1
        
        partialSums = (0,) + tuple(accumulate(nums))
        print(f'{partialSums=}')
        max_sum = max(partialSums)
        print(f'Max Partial Sum: {max_sum}')

        answers = []
        diffs = []
        for i, S in enumerate(partialSums):
            print(f'{i=} {S=}')
            new_diff = (S, i)
            find_K = (S - k, i)
            bisect.insort(diffs, new_diff)
            index = bisect_right(diffs, find_K)
            print(f'  found {S - k} at {index=}')
            possible_J = (
                j
                for ignore_number, j in diffs[:index]
            )
            print(f'  {possible_J=}')
            j = max(possible_J, default=None)
            if j is None:
                print(f'  (no J)')
                continue
            answer = i - j
            print(f'  {j=} {answer=}')
            answers.append(answer)
        print(f'{answers=}')
        return min(answers, default=-1)
        
# NOTE: Acceptance Rate 27.0% (HARD)
# NOTE: yet another version which times out for large inputs
