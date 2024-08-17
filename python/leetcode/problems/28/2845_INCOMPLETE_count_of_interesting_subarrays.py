class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:

        mods = [
            1 if (N % modulo == k) else 0
            for N in nums
        ]
        # print(f'{mods=}')

        partialSums = (0,) + tuple(accumulate(mods))
        # print(f'{partialSums=}')

        answer = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                cnt = partialSums[j+1] - partialSums[i]
                OK = (cnt % modulo == k)
                # print(f'[{i}..{j}]: {cnt=} {OK=}')
                if OK:
                    # print(f'  YES')
                    answer += 1
                # else:
                #     # print(f'  no')

        return answer
# NOTE: Times out for large inputs
