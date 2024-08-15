class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:

        LEN = len(nums1)
        assert LEN == len(nums2)

        dp1 = [None] * LEN
        dp2 = [None] * LEN
        
        dp1[0] = 1  # first element of each list is a length-1 ND group for free
        dp2[0] = 1
        i = 0
        print(f'{i}: {dp1[i]=} {dp2[i]=}')
        for i in range(1, LEN):
            A1 = nums1[i - 1]
            A2 = nums2[i - 1]
            B1 = nums1[i]
            B2 = nums2[i]
            group1 = []
            if B1 >= A1:
                group1.append(
                    dp1[i - 1] + 1
                )
            if B1 >= A2:
                group1.append(
                    dp2[i - 1] + 1
                )
            dp1[i] = max(group1, default=1)     # default b/c we start over: len-1 group
            group2 = []
            if B2 >= A1:
                group2.append(
                    dp1[i - 1] + 1
                )
            if B2 >= A2:
                group2.append(
                    dp2[i - 1] + 1
                )
            dp2[i] = max(group2, default=1)
            print(f'{i}: {dp1[i]=} {dp2[i]=}')
        return max([
            max(dp1),
            max(dp2),
        ])
# NOTE: Runtime 1117 ms Beats 25.00%
# NOTE: Memory 34.44 MB Beats 51.68%
