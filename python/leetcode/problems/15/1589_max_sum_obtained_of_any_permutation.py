class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        mod = 10 ** 9 + 7

        ## Brute force method: works, but Time Limit Exceeded for large inputs
        # requestCounts = Counter((
        #     R
        #     for (A, B) in requests
        #     for R in range(A, B + 1)
        # ))
        # print(f'{requestCounts=}')
        # usage = requestCounts.values()

        ## Smarter method using a Diff array
        diffCount = Counter()
        for (A, B) in requests:
            diffCount[A] += 1
            diffCount[B + 1] -= 1
        print(f'{diffCount=}')
        diffArray = [
            diffCount[N]
            for N in range(len(nums) + 1)
        ]
        print(f'{diffArray=}')
        usage = list(itertools.accumulate(diffArray))
        print(f'{usage=}')

        nums.sort(reverse=True)
        usage.sort(reverse=True)
        print(f'   {nums=}')
        print(f'  {usage=}')
        answers = [
            A * B
            for (A, B) in zip(nums, usage)
        ]
        print(f'{answers=}')
        return sum(answers) % mod

