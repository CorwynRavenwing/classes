class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def can_have_k_nonadjacent_with_max_LT(target: int) -> bool:
            index = 0
            for i in range(k):
                if index >= len(nums):
                    # print(f'No: ran out of nums')
                    return False
                while nums[index] > target:
                    # print(f'(skip {nums[index]} > {target})')
                    index += 1
                    if index >= len(nums):
                        # print(f'No: ran out of nums')
                        return False
                # therefore nums[index] <= target
                # print(f'pick #{i+1}/{k}: [{index}]={nums[index]}')
                index += 2  # jump past the next house
            # print(f'Yes: ran out of K')
            return True
        
        L = min(nums)
        left = can_have_k_nonadjacent_with_max_LT(L)
        if left:
            print(f'Strange, {L=} is true')
            return L
        R = max(nums)
        right = can_have_k_nonadjacent_with_max_LT(R)
        if not right:
            print(f'Strange, {R=} is false')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = can_have_k_nonadjacent_with_max_LT(M)
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

# NOTE: Runtime 742 ms Beats 51.06%
# NOTE: Memory 27.92 MB Beats 20.68%

# NOTE: re-ran for challenge:
# NOTE: Runtime 349 ms Beats 48.95%
# NOTE: Memory 28.64 MB Beats 50.00%
