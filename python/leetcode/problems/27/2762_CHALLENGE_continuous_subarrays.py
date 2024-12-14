class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        answer = 0
        i = 0
        A = nums[i]
        j = 0
        B = nums[j]
        count = Counter([B])
        while i <= j < len(nums):
            # print(f'[{i}..{j}] ({A}..{B}) {count}')
            if max(count) - min(count) <= 2:
                # continuous from A .. B
                # print(f'  continuous: add {j - i + 1} subarrays ending here')
                answer += j - i + 1
                # print(f'  Expand J to right')
                j += 1
                if j >= len(nums):
                    # print(f'Ran out of nums: {j=}')
                    break
                B = nums[j]
                count[B] += 1
                continue
            else:
                # not continuous because of new B
                # print(f'  not continuous: Shrink I from left')
                count[A] -= 1
                if not count[A]:
                    # remove zeros, which would mess up max/min of count
                    del count[A]
                i += 1
                if i >= len(nums):
                    # print(f'Ran out of nums: {i=}')
                    break
                A = nums[i]
                if i > j:
                    print(f'ERROR!  {i=} > {j}, which should be impossible')
                    return -99999
        return answer
# NOTE: Runtime 794 ms Beats 30.77%
# NOTE: Memory 26.96 MB Beats 51.92%
# NOTE: re-ran for challenge, and recieved:
# NOTE: Runtime 831 ms Beats 21.69%
# NOTE: Memory 27.56 MB Beats 28.65%
