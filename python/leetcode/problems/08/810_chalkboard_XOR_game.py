class Solution:
    def xorGame(self, nums: List[int]) -> bool:

        Xor = lambda L: reduce(xor, L)

        nums_xor = Xor(nums)
        print(f'{nums_xor=}')

        nums.sort()

        @cache
        def DP(nums: List[int]) -> bool:
            # print(f'DP({nums}):')
            if not nums:
                # print(f'  WIN A: {nums=}')
                return True
            if len(nums) == 1:
                if not nums[0]:
                    # print(f'  WIN B: {nums=}')
                    return True
                else:
                    # print(f'  LOSE C:{nums=}')
                    return False
            nums_xor = Xor(nums)
            if not nums_xor:
                # print(f'  WIN D: {nums=}')
                return True

            nums_set = set(nums)
            if nums_set == {nums_xor}:
                # no choice but to pick the bad number
                # print(f'  LOSE E:{nums=}')
                return False

            # the following section works, but gives Time Exceeded
            # for large inputs:

            # answers = []
            # for N in tuple(sorted(nums_set)):
            #     # if N == nums_xor:
            #     #     print(f'  {N=}: SKIP')
            #     #     continue
            #     index = nums.index(N)
            #     remain_nums = nums[:index] + nums[index + 1:]
            #     remain_set = nums_set - {N}
            #     # print(f'  [{index}]={N}: {remain_set}={remain_nums}')
            #     remain_xor = xor(N, nums_xor)
            #     if not remain_xor:
            #         # print(f'    (LOSE){remain_xor=}')
            #         answers.append(False)
            #     else:
            #         answer = not DP(remain_nums)
            #         # print(f'DP({nums}): {N=} {answer=}')
            #         answers.append(answer)
            # # print(f'  DEBUG: {answers=}')
            # if True in answers:
            #     # print(f'DP({nums}): WIN H')
            #     print(f'DP({len(nums)}): WIN')
            #     assert len(nums) % 2 == 0
            #     return True
            # else:
            #     # print(f'DP({nums}): LOSE I')
            #     print(f'DP({len(nums)}): LOSE')
            #     assert len(nums) % 2 != 0
            #     return False
            
            # ... but because of the assertions above, we can
            # replace it with:

            return len(nums) % 2 == 0
        
        return DP(tuple(nums))

# NOTE: Acceptance Rate 62.9% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Time Exceeded, needed shortcut)
# NOTE: Runtime 3 ms Beats 26.98%
# NOTE: Memory 18.27 MB Beats 5.56%
