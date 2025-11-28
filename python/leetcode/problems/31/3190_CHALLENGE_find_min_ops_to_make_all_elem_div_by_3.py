class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        mods = [
            N % 3
            for N in nums
        ]
        print(f'{mods=}')
        counts = Counter(mods)
        print(f'{counts=}')
        
        return counts[1] + counts[2]

# NOTE: Acceptance Rate 89.4% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 7 ms Beats 0.26%
# NOTE: Memory 17.94 MB Beats 21.95%
