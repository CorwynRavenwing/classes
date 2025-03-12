class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        signs = [
            (
                '+' if N > 0 else
                '-' if N < 0 else
                '0' if N == 0 else
                '?'
            )
            for N in nums
        ]
        counts = Counter(signs)
        print(f'{counts=}')
        pos = counts['+']
        neg = counts['-']
        return max(pos, neg)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 10 ms Beats 5.12%
# NOTE: Memory 18.18 MB Beats 22.96%
