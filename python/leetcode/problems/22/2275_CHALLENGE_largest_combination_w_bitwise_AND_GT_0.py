class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        
        maxSize = len(f'{max(candidates):b}')
        # print(f'{maxSize=}')
        bitstrings = [
            f'{C:0{maxSize}b}'
            for C in candidates
        ]
        # print(f'{bitstrings=}')

        by_bit = tuple(zip(*bitstrings))
        # print(f'{by_bit=}')

        bit_sums = [
            sum(
                map(int, BB)
            )
            for BB in by_bit
        ]
        # print(f'{bit_sums=}')

        return max(bit_sums)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 675 ms Beats 17.50%
# NOTE: Memory 58.50 MB Beats 5.15%
