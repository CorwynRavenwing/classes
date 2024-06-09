class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        available = {
            0: 1  # total of zero, one time
        }

        for N in nums:
            print(f'{N}: {available}')
            plus = dict([
                (total + N, count)
                for (total, count) in available.items()
            ])
            minus = dict([
                (total - N, count)
                for (total, count) in available.items()
            ])
            available = plus    # start with this data
            for (total, count) in minus.items():
                available.setdefault(total, 0)
                available[total] += count
        print(f'X: {available}')

        available.setdefault(target, 0)
        return available[target]

