class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        @cache
        def pattern_is_in_word(pattern: str) -> bool:
            return (pattern in word)
        
        answer = 0
        for pattern in patterns:
            if pattern_is_in_word(pattern):
                answer += 1
        
        return answer

# NOTE: Acceptance Rate 83.1% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: no cache:
# NOTE: Runtime 4 ms Beats 10.00%
# NOTE: Memory 19.46 MB Beats 6.22%
# NOTE: with cache:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.39 MB Beats 19.78%

