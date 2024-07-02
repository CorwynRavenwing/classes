class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        countNums1 = Counter(nums1)
        countNums2 = Counter(nums2)
        answer = []
        for N, count1 in countNums1.items():
            count2 = countNums2[N]
            MIN = min(count1, count2)
            print(f'{N=} {count1=} {count2=} min={MIN}')
            answer.extend(
                [N] * MIN
            )
        return answer

