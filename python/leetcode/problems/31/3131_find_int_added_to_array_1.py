class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:

        # we borrow some code from #3132, which I did first

        nums1.sort()
        nums2.sort()

        # SHORTCUT 1: X = min(nums2) - min(nums1).
        # Then try adding that attempted X to every value in nums1.
        # all of them should exist in nums2.

        # SHORTCUT 2: we can test this equivalence by subtracting
        # Counter( nums1 with +X applied ) - Counter( nums2 )

        count2 = Counter(nums2)
        print(f'{count2=}')
        answers = []
        Z = nums2[0]
        A = nums1[0]
        X = Z - A
        print(f'{Z=} {A=}: {X=}')
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
        if L == 0:
            answers.append(X)

        print(f'{answers=}')
        return min(answers)

# NOTE: Accepted on first Submit
# NOTE: Runtime 67 ms Beats 6.36%
# NOTE: Memory 16.80 MB Beats 35.83%
