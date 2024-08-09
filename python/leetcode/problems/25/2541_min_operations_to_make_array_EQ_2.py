class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:

        # SANITY CHECKS
        if nums1 == nums2:
            print(f'Yes: already equal')
            return 0
            
        if k == 0:
            print(f'No: {k=}, division by zero')
            return -1
        
        mods1 = [(N % k) for N in nums1]
        mods2 = [(N % k) for N in nums2]
        print(f'{mods1=}')
        print(f'{mods2=}')
        if mods1 != mods2:
            print(f'No: mods are different')
            return -1
        
        diffs = [
            (A - B) // k
            for (A, B) in zip(nums1, nums2)
        ]
        print(f'{diffs=}')
        if sum(diffs) != 0:
            print(f'No: diffs do not sum to 0')
            return -1
        
        posSum = sum([
            D
            for D in diffs
            if D > 0
        ])
        print(f'{posSum=}')
        # negSum = sum([
        #     D
        #     for D in diffs
        #     if D < 0
        # ])
        # # negSum === -posSum because sum(diffs) == 0

        return posSum
# NOTE: Runtime 556 ms Beats 16.47%
# NOTE: Memory 36.84 MB Beats 5.29%
