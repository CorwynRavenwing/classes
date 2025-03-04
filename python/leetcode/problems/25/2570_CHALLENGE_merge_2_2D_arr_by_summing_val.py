class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        answer = Counter()
        for id, val in nums1 + nums2:
            answer[id] += val
        return tuple(
            sorted(
                answer.items()
            )
        )

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 2 ms Beats 29.00%
# NOTE: Memory 17.73 MB Beats 99.24%
