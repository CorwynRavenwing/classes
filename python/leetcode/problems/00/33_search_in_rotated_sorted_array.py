class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L = 0
        R = len(nums) - 1
        M = None
        left = nums[L]
        right = nums[R]
        mid = None
        print(f'{left=} {right=}')
        print(f'{target=}')
        if target == left:
            print(f'Found! {L=}')
            return L
        if target == right:
            print(f'Found! {R=}')
            return R
        if left == right:
            print('  zero-size range')
            return -1
        while (left > right) and (L + 1 < R):
            M = (L + R) // 2
            mid = nums[M]
            print(f'R [L,M,R]=[{L},{M},{R}] = ({left},{mid},{right}) ?={target}')
            if target == mid:
                print(f'  Found! {M=}')
                return M
            if left < target and mid <= right:
                print('  target in left half [A]')
                (R,right) = (M,mid)
                continue
            if left <= mid and target < right:
                print('  target in right half [A]')
                (L,left) = (M,mid)
                continue
            if target < mid < right:
                print('  target in left half [B]')
                (R,right) = (M,mid)
                continue
            if left < mid < target:
                print('  target in right half [B]')
                (L,left) = (M,mid)
                continue
            if left < target < mid:
                print('  target in left half [C]')
                (R,right) = (M,mid)
                continue
            if mid < target < right:
                print('  target in right half [C]')
                (L,left) = (M,mid)
                continue
            if right < target < left:
                print('  target outside of range')
                return -1

            return -999

        # now, since left < right, do a normal binary search:
        while L + 1 < R:
            M = (L + R) // 2
            mid = nums[M]
            print(f'B [L,M,R]=[{L},{M},{R}] = ({left},{mid},{right}) ?={target}')
            if target == mid:
                print(f'  Found! {M=}')
                return M
            elif target < mid:
                print('  target in left half')
                (R,right) = (M,mid)
                continue
            elif target > mid:
                print('  target in right half')
                (L,left) = (M,mid)
                continue
            else:
                raise Exception(f'{(L,M,R)=} {(left,mid,right)=} {target=} cant compare target and mid')
        
        print(f'X [L,M,R]=[{L},--,{R}] = ({left},--,{right}) ?={target}')
        print('  Target not found')
        return -1

