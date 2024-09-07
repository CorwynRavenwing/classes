class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:

        nums1.sort()    # order is irrelevant
        nums2.sort()

        # SHORTCUT 1: You are only deleting two values from nums1.
        # Therefore, at least *one* of the first three values of nums1 *will* remain.
        # Therefore, if nums1 == [ A B C ... ] and nums2 == [ Z ... ],
        # then X will absolutely be one of (Z-A), (Z-B), or (Z-C).
        # Then try adding that attempted X to every value in nums1.
        # all but exactly 2 of them should exist in nums2.

        # SHORTCUT 2: we can test this equivalence by subtracting
        # Counter( nums1 with +X applied ) - Counter( nums2 )

        count2 = Counter(nums2)
        print(f'{count2=}')
        Z = nums2[0]
        answers = []
        for ABC in nums1[:3]:
            X = Z - ABC
            print(f'{Z=} {ABC=}: trial {X=}')
            nums1PlusX = [
                N + X
                for N in nums1
            ]
            print(f'  {nums1PlusX=}')
            count1x = Counter(nums1PlusX)
            print(f'  {count1x=}')
            diff = count1x - count2
            print(f'  {diff=}')
            L = len(tuple(diff.elements()))
            print(f'  {L=}')
            if L == 2:
                answers.append(X)

        print(f'{answers=}')
        return min(answers)

# NOTE: Accepted on first Submit
# NOTE: Runtime 82 ms Beats 46.43%
# NOTE: Memory 17.00 MB Beats 7.54%
