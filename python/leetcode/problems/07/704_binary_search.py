class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L = 0
        R = len(nums) - 1
        left = nums[L]
        right = nums[R]
        if target == left:
            return L
        if target == right:
            return R
        while L + 1 < R:
            M = (L + R) // 2
            mid = nums[M]
            print(f'[{L},{M},{R}] = ({left},{mid},{right})')
            if target == mid:
                return M
            if target < mid:
                (R, right) = (M, mid)
                continue
            if target > mid:
                (L, left) = (M, mid)
        print(f'after loop: [{L},{R}] = ({left},{right})')
        return -1

