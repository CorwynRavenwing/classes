class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        
        marbles = set(nums)
        # print(f'0: {marbles=}')
        for source, dest in zip(moveFrom, moveTo):
            marbles.remove(source)
            marbles.add(dest)
            # print(f'{source}->{dest}: {marbles=}')
        return tuple(sorted(marbles))

# NOTE: Acceptance Rate 50.2% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 41 ms Beats 97.09%
# NOTE: Memory 37.00 MB Beats 56.31%
