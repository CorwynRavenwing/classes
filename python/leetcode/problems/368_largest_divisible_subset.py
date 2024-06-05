class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()
        LDS = [None] * len(nums)
        for i, N in enumerate(nums):
            print(f'[{i}]:{N}')
            possible_LDS = [
                [] + [N]    # this number by itself
            ]
            for j in range(i):
                M = nums[j]
                # print(f'  [{j}]:{M}')
                if N % M == 0:
                    possible_LDS.append(
                        LDS[j] + [N]    # divisor's LDS plus this number
                    )
                # else:
                #     print(f'    {N} !% {M}')
            possible_LDS.sort(
                key=lambda x: len(x),
                reverse=True
            )
            # print(f'  LDSs={possible_LDS}')
            LDS[i] = possible_LDS[0]   # first one == longest
            print(f'  {LDS[i]=}')
        LDS.sort(
            key=lambda x: len(x),
            reverse=True
        )
        print(f'sorted {LDS=}')
        return LDS[0]  # again, first == longest

