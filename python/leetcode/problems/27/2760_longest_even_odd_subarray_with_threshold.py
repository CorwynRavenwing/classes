class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:

        (L, R) = (0, 0)
        max_len = 0
        while L < len(nums) and R < len(nums):
            print(f"{L=} {nums[L]=} %={nums[L] % 2}")
            if nums[L] % 2 != 0:
                L += 1
                continue
            if nums[L] > threshold:
                print(f"  num > {threshold}")
                L += 1
                continue

            R = L + 1
            while R < len(nums):
                print(f"{L=} {R=} {nums[R]=} %={nums[R] % 2}/{nums[R-1] % 2}")
                if (nums[R] % 2) == (nums[R-1] % 2):
                    print(f"  Stop, N[{R}] not even/odd")
                    R -= 1
                    break
                if nums[R] > threshold:
                    print(f"  Stop, N[{R}] > {threshold}")
                    R -= 1
                    break
                R += 1
            segment = nums[L:R+1]
            print(f'    {segment=} [{L}:{R+1}]')
            max_len = max(max_len, len(segment))
            L = max(L, R + 1)   # jump L forward to point of error
        return max_len

