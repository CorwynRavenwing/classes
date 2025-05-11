class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        sum1 = sum(nums1)
        sum2 = sum(nums2)
        count1 = Counter(nums1)[0]
        count2 = Counter(nums2)[0]
        minTotal1 = sum1 + count1   # replace all zeros with ones
        minTotal2 = sum2 + count2

        print(f'{sum1=} {count1=} {minTotal1=}')
        print(f'{sum2=} {count2=} {minTotal2=}')

        if minTotal1 == minTotal2:
            return minTotal1
        elif minTotal1 < minTotal2:
            if count1:
                return minTotal2
            else:
                return -1
        elif minTotal1 > minTotal2:
            if count2:
                return minTotal1
            else:
                return -1

# NOTE: Accepted on first Submit
# NOTE: Runtime 852 ms Beats 21.54%
# NOTE: Memory 35.86 MB Beats 5.17%

# NOTE: re-ran for challenge:
# NOTE: Runtime 855 ms Beats 55.28%
# NOTE: Memory 38.23 MB Beats 5.19%
