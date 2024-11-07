class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def all_predecessors_of(word: str) -> List[str]:
            answer = set([
                word[:i] + word[i+1:]
                for i in range(len(word))
            ])
            return set([
                A
                for A in answer
                if A in words
            ])
        
        APO = {
            word: all_predecessors_of(word)
            for word in words
        }

        @cache
        def DP(word: str) -> int:
            print(f'DP({word}): ?')
            answers = {
                1 + DP(W)
                for W in APO[word]
            }
            print(f'DP({word}): {answers=}')
            retval = max(answers, default=1)
            print(f'DP({word}): {retval=}')
            return retval
        
        answers = {
            DP(word)
            for word in words
        }
        return max(answers)

# NOTE: Accepted on first Submit
# NOTE: Runtime 1075 ms Beats 10.90%
# NOTE: Memory 20.25 MB Beats 16.53%
