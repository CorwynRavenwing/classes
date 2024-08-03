class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        # count ones:
        size = sum(nums)
        print(f'{size=}')

        # make the array non-circular:
        nums += nums[:size]
        # print(f'{nums=}')

        answer = float('+inf')
        zeroCount = 0
        oneCount = 0
        for i in range(size-1, len(nums)):
            # print(f'{i=}')
            if i == size-1:
                # first time through, do a sum
                oneCount = sum(nums[i + 1 - size:i + 1])
                zeroCount = size - oneCount
                # anything not a 1 must be a 0
            else:
                oneCount += nums[i]        # add one new element that moved into window
                oneCount -= nums[i - size] # subtract element that moved out of window
                zeroCount = size - oneCount
            # print(f'  {oneCount=} {zeroCount=}')
            answer = min(answer, zeroCount)
            if answer == 0:
                print(f"It won't get any better than zero")
                break
        return answer
# NOTE: Runtime 649 ms Beats 93.47%
# NOTE: O(N)
# NOTE: Memory 20.29 MB Beats 71.40%
# NOTE: O(1)
