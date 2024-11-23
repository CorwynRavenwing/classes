class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        @cache
        def DP(cards: List[int], k: int) -> int:
            if k == 0:
                return 0
            
            return max([
                cards[0] + DP(cards[1:], k - 1),
                cards[-1] + DP(cards[:-1], k - 1),
            ])
        
        cards = tuple(cardPoints)   # make it hashable
        return DP(cards, k)

# NOTE: Accepted on first Run
# NOTE: without cache: Time Limit Exceeded
# NOTE: with cache: Memory Limit Exceeded
# NOTE: trying a different method entirely
