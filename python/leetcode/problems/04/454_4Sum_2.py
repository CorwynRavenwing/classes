class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        def allSums(nums1: List[int], nums2: List[int]) -> List[int]:
            # calculate all sums: O(N^2) time,space:
            nums3 = [
                A + B
                for A in nums1
                for B in nums2
            ]
            return nums3
        
        list_1_2 = allSums(nums1, nums2)
        list_3_4 = allSums(nums3, nums4)
        # count of each value: O(N) time,space:
        count_1_2 = Counter(list_1_2)
        count_3_4 = Counter(list_3_4)
        # find intersection: O(N) time, O(1) space
        answer = 0
        for (A, countA) in count_1_2.items():
            print(f'{A=}')
            countB = count_3_4[-A]  # invert sign of A
            print(f'  {countA} {countB}')
            answer += (countA * countB)
        
        # entire solution: O(N^2) time,space
        return answer

# NOTE: no code from prior version, which is entirely different
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 403 ms Beats 74.74%
# NOTE: Memory 18.66 MB Beats 5.04%
