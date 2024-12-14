class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        Sqrt = lambda x: int(math.sqrt(x))

        gifts.sort()    # because order is irrelevant
        
        print(f'{0}: {gifts}')
        for i in range(1, k + 1):
            G = gifts.pop(-1)   # highest
            G = Sqrt(G)
            bisect.insort(gifts, G)
            # print(f'{i}: {gifts}')
        
        print(f'{i}: {gifts}')
        return sum(gifts)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 7 ms Beats 49.64%
# NOTE: Memory 17.54 MB Beats 8.46%
