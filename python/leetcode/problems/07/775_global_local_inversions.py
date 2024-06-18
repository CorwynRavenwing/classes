class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # answer = True
        # for i, N in enumerate(nums):
        #     # print(f'[{i}]={N}')
        #     fragment = nums[i+2:]
        #     # print(f'  {fragment}')
        #     if fragment:
        #         if min(fragment) < N:
        #             print(f'    NON-LOCAL')
        #             answer = False
        #         # else:
        #         #     print(f'    ok')
        #     # else:
        #     #     print(f'    empty')
        # return answer

        # this works but times out for large inputs.
        # the following is equivalent:

        for i, N in enumerate(nums):
            # print(f'[{i}]={N}: {N-i}')
            if N-i in [-1, 0, 1]:
                continue
            print(f'[{i}]={N}: {N-i}')
            print(f'  FAIL')
            return False
        return True

# NOTE: 592 ms; Beats 88.82% of users with Python3
