class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()

        def pairSumLEtarget(target: int) -> bool:
            scratch = nums[:]   # copy

            while scratch:
                minimum = scratch[0]    # view the lowest value
                A = scratch.pop(-1)     # consume the highest value
                B_max = target - A          # A + B_max = target
                if B_max < minimum:
                    # print(f'{A=} {B_max=} {minimum=} FAIL')
                    return False
                if B_max == minimum:
                    # print(f'{A=} {B_max=} [{0}]B={B_max}')
                    B_max = scratch.pop(0)
                    continue
                # B_max > minimum:
                index = bisect_right(scratch, B_max) - 1
                B = scratch.pop(index)  # consume the matching value
                # print(f'{A=} {B_max=} [{index}]{B=}')

            return True

        L = 0
        left = pairSumLEtarget(L)
        if left:
            print(f'Strange, {L=} is true')
            return L
        R = 2 * max(nums) + 1
        right = pairSumLEtarget(R)
        if not right:
            print(f'Strange, {R=} is false')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = pairSumLEtarget(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Right')
                (R, right) = (M, mid)
            else:
                print(f'  False: replace Left')
                (L, left) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # R is now the lowest possible True value
        return R

# NOTE: prior version, binary search for the matching pair.
# NOTE: O(N log N), gets a Time Limit Exceeded error.
