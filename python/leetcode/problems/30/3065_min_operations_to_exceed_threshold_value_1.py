class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        counts = Counter(nums)
        print(f'{counts=}')

        answer = sum([
            count
            for num, count in counts.items()
            if num < k
        ])

        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 61 ms Beats 7.14%
# NOTE: Memory 16.65 MB Beats 29.82%
