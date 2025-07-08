class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        counts = Counter(arr)
        print(f'{counts=}')

        lucky = [
            value
            for value, count in counts.items()
            if value == count
        ]
        print(f'{lucky=}')
        return max(lucky, default=-1)

# NOTE: Acceptance Rate 69.7% (easy)

# NOTE: Accepted on second Run (max needed default for null answer)
# NOTE: Accepted on first Submit
# NOTE: Runtime 1 ms Beats 46.59%
# NOTE: Memory 17.96 MB Beats 31.09%
