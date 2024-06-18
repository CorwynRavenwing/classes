class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        nums.sort()
        # bucket = []
        max_bucket = None
        answer = 0
        while nums:
            N = nums.pop(0)
            print(f'{N=} ({max_bucket})')
            if max_bucket is None:
                max_bucket = N - 1  # prime with lower number
            if N <= max_bucket:
                new_N = max_bucket + 1
                answer += (new_N - N)
                N = new_N
                print(f'  ->{N}')
            max_bucket = N
            # bucket.append(N)
        # print(f'{bucket=}')
        return answer

