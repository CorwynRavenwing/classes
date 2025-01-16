class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        # SHORTCUT 1: since XOR is its own inverse, if we XOR
        # something twice, it throws both away.

        # SHORTCUT 2: each item in nums1 contributes to the answer
        # len(nums2) times; each item in nums2 contributes len(nums1) times.

        # SHORTCUT 3: if these lengths are odd, this is the equivalent
        # of contributing once; if even, the numbers do not contribute at all.

        answer = 0
        if len(nums2) % 2 == 1:
            print(f'{len(nums2)} odd: adding nums1')
            for N in nums1:
                answer ^= N
        if len(nums1) % 2 == 1:
            print(f'{len(nums1)} odd: adding nums2')
            for N in nums2:
                answer ^= N
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 7 ms Beats 39.88%
# NOTE: Memory 35.84 MB Beats 90.17%
