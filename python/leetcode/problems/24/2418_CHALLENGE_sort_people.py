class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return map(lambda x: x[1], sorted(zip(heights, names), reverse=True))
# NOTE: yes, this is a one-liner!!!
# NOTE: Runtime 95 ms Beats 93.45%
# NOTE: O(N log N)
# NOTE: Memory 17.03 MB Beats 45.10%
# NOTE: O(N)
