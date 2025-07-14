class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        counts = Counter(nums)
        max_count = max(counts.values())
        print(f'{counts=}')
        print(f'{max_count=}')

        answer = [[] for i in range(max_count)]
        for value, count in counts.items():
            for i in range(count):
                answer[i].append(value)
        print(f'{answer=}')

        return answer

# NOTE: Acceptance Rate 86.3% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 7 ms Beats 18.71%
# NOTE: Memory 17.93 MB Beats 23.84%
