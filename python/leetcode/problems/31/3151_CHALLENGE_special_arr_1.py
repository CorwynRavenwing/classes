class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        parity = [
            N % 2
            for N in nums
        ]
        print(f'{parity=}')

        pairs = tuple(pairwise(parity))
        print(f'{pairs=}')

        sums = tuple(map(sum, pairs))
        print(f'{sums=}')

        return (
            False
            if 0 in sums
            else False
            if 2 in sums
            else True
        )

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 7 ms Beats 1.38%
# NOTE: Memory 18.08 MB Beats 12.54%
