class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:

        counts = Counter(nums)
        ones = counts[1]
        if ones in [0, 1]:
            print(f'there are {ones=}: no splits')
            return ones
        # now, there is at least one 1 in the list
        # delete all leading 0s
        index = nums.index(1)
        nums = nums[index:]
        print(f'no leading 0s: {nums=}')

        REV = lambda x: tuple(reversed(tuple(x)))

        nums = REV(nums)
        # delete all trailing 0s
        index = nums.index(1)
        nums = nums[index:]
        nums = REV(nums)
        print(f'no trailing 0s: {nums=}')
        joined = ''.join(map(str, nums))
        print(f'{joined=}')
        pieces = joined.split('1')
        print(f'{pieces=}')
        lengths = tuple(map(len, pieces))
        print(f'{lengths=}')
        factors = [X + 1 for X in lengths if X]
        print(f'{factors=}')

        mod = 10 ** 9 + 7

        return math.prod(factors) % mod
# NOTE: Accepted on first Submit
# NOTE: Runtime 2159 ms Beats 7.01%
# NOTE: Memory 27.52 MB Beats 5.17%
