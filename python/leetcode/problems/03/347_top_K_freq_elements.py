class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        freq = counts.most_common(k)
        answer = [
            value
            for value, count in freq
        ]
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 90 ms Beats 50.13%
# NOTE: Memory 21.21 MB Beats 45.09%
