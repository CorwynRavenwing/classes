class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        def Triangle(N: int) -> int:
            return (N) * (N + 1) // 2

        # SHORTCUT: we don't actually care about the numbers,
        # just whether something is or is not zero.

        zeros = [
            ('*' if N == 0 else ' ')
            for N in nums
        ]
        print(f'{zeros=}')
        zeros = ''.join(zeros)
        print(f'{zeros=}')
        zeros = zeros.split(' ')
        print(f'{zeros=}')
        zeros = tuple(map(len, zeros))
        print(f'{zeros=}')
        subarrays = tuple(map(Triangle, zeros))
        print(f'{subarrays=}')

        return sum(subarrays)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 116 ms Beats 5.04%
# NOTE: Memory 28.81 MB Beats 6.40%
