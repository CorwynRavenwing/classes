class Solution:

    cache_limit = 350
    #    10 -> 5474 5403 5547 5313 5829
    #    20 -> 5284 5443 5710 5577 5838
    #    50 -> 5544 5549 5466 5582 5870
    #   100 -> 5270 5408 5713 6028 6465
    #   200 -> 5509 5159 5354 5584 5710 Submit=TLE
    #   300 -> 4894 5076 5191 5045 4847 Submit=TLE
    #   350 ->                          Submit=TLE sometimes and MLE sometimes FFS
    #   375 ->                          Submit=MLE @36
    #   400 -> 4638 5118 4680 5432 5159 Submit=MLE
    #   500 -> 4824 4498 4427 4647 4548 Submit=MLE
    #   600 -> MLE
    #   700 -> MLE
    #  1000 -> MLE
    # 10000 -> MLE
    prefix_cache = {}

    # @cache
    # Caching this causes Memory Exceeded;
    # Not caching causes Time Exceeded
    # So we hand-roll a partial cache
    def prefixes(self, word) -> list[str]:
        if len(word) <= self.cache_limit:
            if word in self.prefix_cache:
                return self.prefix_cache[word]
        
        # print(f'prefixes({word})')
        if len(word) == 1:
            return (word,)
        elif len(word) == 0:
            return ()
        truncated = word[:-1]   # all letters except last

        answer = self.prefixes(truncated) + (word,)

        if len(word) <= self.cache_limit:
            self.prefix_cache[word] = answer
        return answer

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        scores = Counter()
        for W in words:
            pref = self.prefixes(W)
            scores.update(pref)
        
        # return [-99999]

        answer = [
            sum([
                scores[P]
                for P in self.prefixes(W)
            ])
            for W in words
        ]
        # print(f'{answer=}')
        return answer

# NOTE: with too much caching, we get Memory Limit Exceeded
# NOTE: with too little caching, we get Time Limit Exceeded
# NOTE: with just the right amount of caching, we get MLE sometimes
#       and TLE sometimes.  Clearly this algorithm is not efficient
#       enough for this project. 
