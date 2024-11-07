class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()

        while len(stones) > 1:
            A = stones.pop(-1)
            B = stones.pop(-1)
            C = abs(A - B)
            print(f'{A}x{B} -> {C}')
            if C:
                bisect.insort(stones, C)
        
        return stones[0] if stones else 0

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was an unexpected edge case)
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.82 MB Beats 17.90%
