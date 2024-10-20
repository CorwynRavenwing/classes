class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        # we borrow some code from #205:

        def getPattern(s: str) -> List[int]:
            print(f'pattern({s}):')
            answer = []
            mappings = {}
            nextValue = 0
            for char in s:
                if char not in mappings:
                    nextValue += 1
                    print(f'  "{char}" -> {nextValue}')
                    mappings[char] = nextValue
                answer.append(mappings[char])
            answer = tuple(answer)
            print(f'-> {answer}')
            return answer
        
        myPattern = getPattern(pattern)
        
        return [
            word
            for word in words
            if myPattern == getPattern(word)
        ]

# NOTE: Re-used entire prior version with small changes in glue code
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 99.39%
# NOTE: Memory 16.60 MB Beats 52.32%
