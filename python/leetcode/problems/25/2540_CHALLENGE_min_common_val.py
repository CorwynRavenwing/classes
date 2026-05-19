class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                _ = nums1.pop(0)
            elif nums1[0] > nums2[0]:
                _ = nums2.pop(0)
            elif nums1[0] == nums2[0]:
                return nums1[0]
            else:
                raise Exception(f'Error: {nums1[0]=} <=> {nums2[0]=} incomparable')
        
        return -1

# NOTE: Acceptance Rate 58.1% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 915 ms Beats 5.07%
# NOTE: Memory 37.38 MB Beats 99.25%
