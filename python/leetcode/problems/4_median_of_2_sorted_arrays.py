class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        count = len(nums1) + len(nums2)
        stupid_way = sorted(nums1 + nums2)
        print(f'{stupid_way=}')
        midpoint = (0 + (count - 1)) // 2
        is_odd = count % 2 == 1
        print(f'{0}, {midpoint=} {count=} {is_odd=}')
        if is_odd:
            return stupid_way[midpoint]
        else:
            middle_two = stupid_way[midpoint:midpoint+2]
            print(f'average of {middle_two}')
            return sum(middle_two) / 2

# 76ms: Beats79.98% of users with Python3
# clearly, the stupid way works

