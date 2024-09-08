class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        # NOTE: once again, they are using "parity" to mean even-or-odd-ness

        parity = [
            N % 2
            for N in nums
        ]
        print(f'{parity=}')

        special = [
            A != B
            for A, B in pairwise(parity)
        ]
        print(f'{special=}')

        return all(special)

# NOTE: Accepted on first Submit
# NOTE: Runtime 52 ms Beats 59.68%
# NOTE: Memory 16.52 MB Beats 53.74%
