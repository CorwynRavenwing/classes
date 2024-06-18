class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        
        (L, R) = (0, 0)
        max_len = 0
        while L < len(nums) - 1 and R < len(nums):
            print(f"{L=} {nums[L]=} {nums[L+1]=}")
            if nums[L] + 1 != nums[L+1]:
                L += 1
                continue

            # already checked L + 1 case above
            R = L + 2
            while R < len(nums):
                print(f"{L=} {R=} {nums[R]=} {nums[R-2]=}")
                if nums[R] != nums[R-2]:
                    print(f"  Stop, N[{R}] not alternating")
                    R -= 1
                    break
                R += 1
            segment = nums[L:R+1]
            print(f'    {segment=} [{L}:{R+1}]')
            assert len(segment) > 1
            max_len = max(max_len, len(segment))
            # L = max(L, R + 1)   # jump L forward to point of error
            L += 1
        return (
            max_len
            if max_len
            else
            -1
        )

